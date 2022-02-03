from django.shortcuts import render
from foodblog.models import Comment, Posts

# Create your views here.

def home(request):
    allPosts = Posts.objects.order_by("-created_at")
    context = {'allPosts':allPosts}
    return render(request,'home.html', context)

def base(request):
    return render(request,'base.html')

def aboutus(request):
    return render(request,"aboutus.html")

def searched(request):
    searched = request.GET['searched']
    allSearched = Posts.objects.filter(content__icontains=searched)
    param = {'allSearched':allSearched}
    return render(request,"searched.html",param)

def singleblog(request, slug):
    try:
        singlepost = Posts.objects.get(slug=slug)
        allcomm = Comment.objects.all().filter(comid=singlepost)
        if request.method=="POST":
            commname=request.POST.get('name','')
            commsec=request.POST.get('message','')
            comment=Comment(comid=singlepost,commname=commname,commsec=commsec)
            comment.save()
        data={'singlepost':singlepost,'allcomm':allcomm}
        return render(request,'singleblog.html',data)
    except Posts.DoesNotExist:
        searched = request.GET['searched']
        allSearched = Posts.objects.filter(content__icontains=searched)
        param = {'allSearched':allSearched}
        return render(request,"searched.html",param)