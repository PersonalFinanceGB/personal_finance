#from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def test(request):
    return HttpResponse ('Всё работает. Пользователь, '+ str(request.user)+' , приветствуем тебя!') 




