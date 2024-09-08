from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : '24/25 Away Kit',
        'price': '1000000',
        'description': 'Manchester United Away Kit for the 24/25 Season',
        'quantity': '10',
        'sold': '7'
    }

    return render(request, "main.html", context)