from django.shortcuts import render

# Create your views here.
def sweety(request):
    return render(request,'sweety.html')


def raj(request):
    return render(request,'raj.html') 


def sweety2(request):
    return render(request,'sweety2.html')
