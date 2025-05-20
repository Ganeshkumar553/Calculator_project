from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def done(request):
#     return HttpResponse("New project")
def done(request):
    output=""
    if request.method=="POST":
        num1=eval(request.POST.get("fn"))
        num2=eval(request.POST.get("sn"))
        opr=request.POST.get("opr")
        if opr=="+":
            output=num1+num2
        elif opr=="-":
            output=num1-num2
        elif opr=="*":
            output=num1*num2
        elif opr=="/":
            output=num1/num2

    return render(request,"form.html",{'o':output})

# def done(request):
#     return render(request,"form.html")