from django.shortcuts import render

def menu(request):
    food = {'name': 'french fries', 'price': 30, 'comment': 'Great!'}
    return render(request, 'menu.html', {"food":food})
