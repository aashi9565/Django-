from django.shortcuts import render ,HttpResponse ,redirect


from . models import signup_data

# Create your views here.

def home(req):
    return render(req,'home.html')



def about(req):
    return render(req,'about.html')


def signup(req):
    if req.method=="GET":
        return render(req,'signup.html')
    else:
        fname=req.POST.get('fname')
        lname=req.POST.get('lname')
        email=req.POST.get('email')
        mobile=req.POST.get('mobile')
        password=req.POST.get('pass')
        print(fname,lname,email,password)
        if signup_data.objects.filter(email=email).exists():
            msg="email already exist"
            return render (req,"signup.html",{"key" : msg })
        else:
            ob=signup_data(fname=fname,lname=lname,email=email,password=password)
            ob.save()
            return redirect("/login")
def login(req):
    if req.method=="GET":
        return render (req,"login.html")
    else:
        email=req.POST.get("email")
        password=req.POST.get("pass")
        #print(email,password)
        if signup_data.objects.filter(email=email).exists():
            if(signup_data.objects.filter(email=email,password=password)):
                data=signup_data.objects.get(email=email)
                return render(req,"profile.html",{"key":data})
            else:
                msg="invaild password"
                return render(req,"login.html",{"key":msg})
        else:
            msg="email dosent exist"
            return render(req,"login.html",{"key":msg})
