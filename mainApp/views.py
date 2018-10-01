from django.shortcuts import render

def index(request):
  return render(request, 'mainApp/homePage.html')

def contact(request):
  return render(request, 'mainApp/basic.html', {'values': ['Если у вас остались вопросы, то задавайте их мне по телефону','(000)000-00-00', 'examples@mail.ru']})