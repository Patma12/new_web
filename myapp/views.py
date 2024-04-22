from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required #บังสคับล็อคอิน

# Create your views here.

def Home(request):
    return render(request,'myapp/home.html')


def Contact(request):
    return render(request,'myapp/contact.html')

def AboutUs(request):
    return render(request,'myapp/about_us.html')

def TrackingPage(request):
    tracking = Tracking.objects.all()
    context = {'tracking':tracking}
    return render(request,'myapp/tracking.html',context)

def AskPage(request):
    if request.method == 'POST':
        data = request.POST.copy()
        # 
        name = data.get('name')
        email = data.get('email')
        title = data.get('title')
        detail = data.get('detail')
        print(name,email,title,detail)

        new = Ask()
        new.name = name
        new.email = email
        new.title = title
        new.detail = detail
        new.save()
    return render(request,'myapp/ask.html')

@login_required
def QuestionsgPage(request):
    questions = Ask.objects.all()
    context = {'questions':questions}
    return render(request,'myapp/questions.html',context)




