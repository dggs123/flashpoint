from django.shortcuts import render, redirect
from .models import photo
from django.http import HttpResponse,HttpResponseRedirect
import shutil
import os
import glob

def get_filepaths(directory):
    """
    This function will generate the file names in a directory
    tree by walking the tree either top-down or bottom-up. For each
    directory in the tree rooted at directory top (including top itself),
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.
    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_1=[filepath,filename]
            file_paths.append(file_1)  # Add it to the list.

    return file_paths  # Self-explanatory.
# Create your views here.
def home(request):
    try:
        x=[]
        toprank = photo.objects.order_by("-nlikes")[:5]
        choices = photo.objects.order_by("?")[:2]
#        if choices1.tag =='c':
#            choices2=photo.objects.filter(tag="c").order_by("?")[:2]
#        else:
#            choices2=photo.objects.filter(tag="n").order_by("?")[:2]
        for ch in choices:
            x.append(ch)
        context={"choices1":x[0],"choices2":x[1],"topr":toprank}
        return render(request,"home.html",context)
    except IndexError:
        return HttpResponse("!!!!!ERROR!!!!!")

def incre(request,id=None):
    win_obj=photo.objects.get(id=id)
    win_obj.nlikes+=1
    win_obj.save()
    return redirect('/')

def top(request):
    choices = photo.objects.order_by("-nlikes")[:50]
    context = {"choice": choices}
    return render(request, "top.html", context)

def add(request):
    # Run the above function and store its results in a variable.
    full_file_paths = get_filepaths("C:\\Users\\gaurav\\Videos\\_media_cdn_\\add")
    pre="gallery\\"
    for file_path in full_file_paths:
        shutil.move(file_path[0],("C:\\Users\\gaurav\\Videos\\_media_cdn_\\gallery\\"+file_path[1]))
        first_string,second=file_path[1].split(".")
#        first_string,third=first_string.split("_")
#        p=photo(Name=first_string,image=(pre+file_path[1]),tag=third)
        p=photo(Name=first_string,image=(pre+file_path[1]))
        p.save()
    return HttpResponse("YOURS FILES UPDATED THANKS!!")