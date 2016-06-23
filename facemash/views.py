from django.shortcuts import render
from .models import photo,total_likes
# Create your views here.
def home(request):
    if request.method == "POST":
        win=request.POST['winner']
        lose=request.POST['loser']
        win_obj=photo.objects.get(id=win)
        win_obj.nlikes+=1
        win_obj.save()
    choices = photo.objects.order_by("?")[:2]
    x = []
    for ch in choices:
        x.append(ch)
    context={"choices1":x[0],"choices2":x[1]}
    return render(request,"home.html",context)
def top(request):
    choices = photo.objects.order_by("-nlikes")[:10]
    context = {"choice": choices}
    return render(request, "top.html", context)
