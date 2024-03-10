from django.shortcuts import render,HttpResponse

def sample1(request):
    return render(request,"index.html")

def sample2(request):
    return render(request,"destination.html")

def sample3(request):
    return render(request,"travel.html")

def sample4(request):
    return render(request,"login.html")

def sample5(request):
    return render(request,"regester.html")

def sample6(request):
    return render(request,"user.html")

def sample7(request):
    return render(request,"contact.html")

def sample8(request):
    return render(request,"about.html")