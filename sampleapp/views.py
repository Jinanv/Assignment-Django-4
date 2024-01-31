from django.shortcuts import render,redirect
from .models import log,reg
from .form import AddForm

# Create your views here.

def index(request):
    return render(request,"index.html")

def register(request):
    return render(request,"register.html")

def insert(request):

    if request.method=='POST':
        username = request.POST.get('username')
        age = request.POST.get('age')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conform_password = request.POST.get('conform_password')
        log(username=username,age=age,email=email,password=password,conform_password=conform_password).save()
    return render(request,"register.html")

def view(request):
    cr=log.objects.all()
    return render(request,"view.html",{'cr':cr})

def detailview(request,pk):
    cr=log.objects.get(id=pk) 
    return render (request,"detailedview.html",{'cr':cr})

def delete(request,pk):
    cr=log.objects.get(id=pk)
    cr.delete()
    return redirect("/")

def update(request,pk):
    cr = log.objects.get(id = pk)
    form = AddForm(instance = cr)
    if request.method =='POST':
        form =  AddForm(request.POST,instance=cr)
        if form.is_valid:
            form.save()
            return redirect("/")
    return render(request,"update.html",{'form':form})

def loginn(request):
    return render(request,"login.html")

def userlog(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        cr = reg.objects.filter(username=username,password=password)
        if cr:

            user_details=reg.objects.get(username=username,password=password)
            id=user_details.id
            username=user_details.username
            email=user_details.email

            request.session['id'] = id
            request.session['username'] = username
            request.session['password'] = email

            return redirect('welcome')
        else:
            return render(request,'login.html',{'wrong':"Wrong User name or password"})
    else:
        return render(request,'view.html')
    

def welcome(request):
    id=request.session['id']
    username=request.session['username']
    password=request.session['password']
    return render(request,"login.html",{'id':id,'username':username,'password':password})

def logout (request):
    return redirect('login')