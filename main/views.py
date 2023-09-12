from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Tiva Adhisti Nafira Putri',
        'class': 'PBP KI'
    }

    return render(request, 'main.html', context)