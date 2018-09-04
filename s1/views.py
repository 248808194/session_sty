from django.shortcuts import render,HttpResponse
from django.shortcuts import redirect

# Create your views here.


def login(request):
    print(123)
    if request.method == 'GET':
        return  render(request,'login.html')

    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        print(u,p)
        if u == 'root' and p == '123123':
            request.session['username'] = u
            request.session['is_login'] = True
            return  redirect('/s1/index')
        else:
            return render(request,'login.html')


def index(request):
    if request.session.get('is_login',None):
        return  render(request,'index.html')
    else:
        return redirect('/s1/login')



def logout(request):
    request.session.clear() #删除用户所有的session数据
    return redirect('/s1/login')



def sg(request):
    from s1 import models
    obj = models.UserInfo(user='zhoutao')
    obj.save()
    print('end')

    obj = models.UserInfo(user='root')
    obj.save()


    return HttpResponse(200)
