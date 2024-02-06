from django.shortcuts import render
from app.models import place
def home(request):
    p=place.objects.all()
    t=Team.objects.all()
    return render(request,'base.html',{'p':p,'t':t})
