from django.shortcuts import render
from .models import Place
from .models import Nature
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    nat=Nature.objects.all()
    return render(request,"index.html",{'result':obj,'results':nat})
