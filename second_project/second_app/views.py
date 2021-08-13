from django.shortcuts import render
from second_app.models import Userid
# Create your views here.
def home(request):
    return render(request,'second_app/home.html')

def user(request):
    user_list = Userid.objects.order_by('name')
    my_dict = {'u':user_list}
    return render(request,'second_app/data.html',context=my_dict)
