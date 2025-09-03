from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'npm' : '2406495571',
        'name': 'Akhtar Eijaz Putranto',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
