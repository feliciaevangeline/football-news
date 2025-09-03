from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406437054',
        'name': 'Felicia Evangeline Mubarun',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
