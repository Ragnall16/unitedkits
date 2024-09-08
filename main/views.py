from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : '23/24 Home Kit',
        'price': '1000000',
        'description': 'Manchester United Home Kit for the 23/24 Season',
        'quantity': '10',
        'sold': '7'
    }

    return render(request, "main.html", context)