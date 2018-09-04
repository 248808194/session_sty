from django.shortcuts import render,HttpResponse
from django.shortcuts import redirect

# Create your views here.
from  django import forms
from django.forms import widgets #所有的插件
from django.forms import  fields #所有的字段

class FM(forms.Form):
    user = fields.CharField(
        error_messages={'required':'用户名不能为空'},
        label='用户名',
        widget=widgets.Input(attrs={'class':'c1'}), #其实就是类型,可以是input 可以是textarea,可以是select; attrs 为该标签加上class=c1的样式
        # widget=widgets.Textarea
    )

    pwd = fields.CharField(
        max_length=12,
        min_length=6,
        error_messages={'required': '密码不能为空.', 'min_length': '密码长度不能小于6', "max_length": '密码长度不能大于12'}, #自定义错误提示信息
        label='密码',
        widget=widgets.PasswordInput
    )

    email = fields.EmailField(
        error_messages={'required': '邮箱不能为空.','invalid':"邮箱格式错误"},
        label='邮箱',

    )
    f = fields.FileField(
        allow_empty_file=False
    )

    city1 = fields.ChoiceField(
        choices=[(0,'上海'),(1,'广州'),(2,'东莞')]
    )
    city2 = fields.MultipleChoiceField(
        choices=[(0,'上海'),(1,'广州'),(2,'东莞')]
    )



def fm(request):
    if request.method == 'GET':
        dic = {  #dic为模拟从数据库拿到的用户信息 ;访问url: http://127.0.0.1:8000/FM/fm?pid=1 ,
            "user": 'r1',
            'pwd': '123123',
            'email': 'sdfsd',
            'city1': 1,
            'city2': [1,2] #多选列表形式
        }
        obj = FM(initial=dic)
        return render(request,'fm.html',{'obj':obj}) #obj在get的时候也要传递,不然页面看不到input框

    elif request.method == 'POST':
        obj = FM(request.POST) #难道post所有数据
        r1 = obj.is_valid() #验证form数据是否提交成功   #成功为True,不成功为False
        if r1:
            print('拿到所有的正确信息',obj.cleaned_data) #拿到所有的正确信息
            from FM import models
            # models.UserInfo.objects.create(**obj.cleaned_data) #如果信息都正确直接在数据库中创建数据,用户则注册成功
        else:
            print('所有的错误信息',obj.errors) #拿到所有的错误信息


    return HttpResponse(200)



def uploadfile(request):
    if request.method == 'GET':
        return  render(request,'uploadfile.html')

    elif request.method == 'POST':
        obj = request.FILES.get('filename')
        print(obj,type(obj))

        with open(obj.name,'wb') as f1:
            for i in obj.chunks():
                f1.write(i)

        return HttpResponse(200)








