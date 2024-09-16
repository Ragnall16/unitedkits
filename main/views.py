from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name' : 'Gopedia',
        'nama' : 'Ragnall Muhammad Al Fath',
        'npm' : '2306210550',
        'kelas' : 'PBP C',
        'name' : '24/25 Away Kit',
        'price': '1000000',
        'description': 'Manchester United Away Kit for the 24/25 Season',
        'stock': '10',
        'sold': '7'
    }

    return render(request, "main.html", context)