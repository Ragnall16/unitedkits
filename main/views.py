import datetime
import os
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.shortcuts import render, redirect
from main.forms import ECommerceForm, JerseyForm
from main.models import ECommerce
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import json
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Not available')
    context = {
        'app_name' : 'UnitedKits',
        'nama' : request.user.username,
        'npm' : '2306210550',
        'kelas' : 'PBP C',
        'last_login': last_login,
    }

    return render(request, "main.html", context)

@login_required(login_url='/login')
def your_order(request):
    return render(request, 'your_order.html')

def products(request):
    form = JerseyForm()
    image_filename = None

    if request.method == 'POST':
        form = JerseyForm(request.POST)
        if form.is_valid():
            season = form.cleaned_data['season']
            jersey_type = form.cleaned_data['type']
            image_filename = f"{season} {jersey_type}.png".replace("/", " ")

    context = {
        'form': form,
        'image_filename': image_filename
    }
    return render(request, 'products.html', context)

def images(request):
    image_dir = os.path.join(settings.STATIC_ROOT, 'image/players/')

    images = [f for f in os.listdir(image_dir) if f.endswith(('jpg', 'jpeg', 'png', 'gif'))]

    context = {'images': images}
    return render(request, 'images.html', context)

@login_required(login_url='/login')
def create_order(request):
    form = ECommerceForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        order_entry = form.save(commit=False)
        order_entry.user = request.user
        order_entry.save()
        return redirect('main:your_order')

    context = {'form': form}
    return render(request, "create_order.html", context)

@login_required(login_url='/login')
def edit_order(request, id):
    # Get order berdasarkan id
    order = ECommerce.objects.get(pk = id)

    # Set order sebagai instance dari form
    form = ECommerceForm(request.POST or None, instance=order)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:your_order'))

    context = {'form': form}
    return render(request, "edit_order.html", context)

@login_required(login_url='/login')
def delete_order(request, id):
    # Get order berdasarkan id
    order = ECommerce.objects.get(pk = id)
    # Hapus order
    order.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:your_order'))

def show_xml(request):
    data = ECommerce.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ECommerce.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ECommerce.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ECommerce.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:show_main')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
@require_POST
def add_order_ajax(request):
    name = strip_tags(request.POST.get("name"))
    season = request.POST.get("season")
    type = request.POST.get("type")
    description = strip_tags(request.POST.get("description"))
    quantity = request.POST.get("quantity")
    size = request.POST.get("size")
    user = request.user

    new_order = ECommerce(
        name=name, season=season,
        type=type, description=description,
        quantity=quantity, size=size,
        user=user
    )
    new_order.save()

    return HttpResponse(b"CREATED", status=201)

def get_form_fields(request):
    form = ECommerceForm()  
    return render(request, 'form_fields_template.html', {'form': form})

@csrf_exempt
def create_order_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_mood = ECommerce.objects.create(
            user=request.user,
            name=data["name"],
            quantity=int(data["quantity"]),
            description=data["description"]
        )
        new_mood.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)