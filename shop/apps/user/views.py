from django.shortcuts import render, redirect
from django.views import View

from user import set_password
from user.forms import UsersForm, LoginForm
from user.helps import check_login
from user.models import User


# 个人中心
@check_login
def member(request):  # ^$
    return render(request, 'user/member.html')


# 登陆
class LoginView(View):
    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        # 接收参数
        data = request.POST
        # 创建form对象
        form = LoginForm(data)
        # 判断参数合法性
        if form.is_valid():
            # 合法
            # 创建session
            request.session['ID'] = form.cleaned_data.get('telephone')
            # 账号密码正确,跳转到首页
            return redirect('commodity:首页')
        else:
            # 不合法,返回错误提示
            errors = form.errors
            return render(request, 'user/login.html', context=errors)


# 注册
class RegView(View):
    def get(self, request):
        # 展示登录表单
        return render(request, 'user/reg.html')

    def post(self, request):
        # 获取数据
        data = request.POST
        # 创建form对象
        form = UsersForm(data)
        if form.is_valid():
            # 合法
            # 获取清洗后的数据
            cleaned_data = form.cleaned_data
            telephone = cleaned_data.get('telephone')
            password = set_password(cleaned_data.get('password'))
            User.objects.create(telephone=telephone, password=password)
            # 保存成功,跳转到登陆
            return redirect('user:登录')
        else:
            errors = form.errors
            return render(request, 'user/reg.html', context=errors)


# 忘记密码
@check_login
def forgetpassword(request):  # ^forgetpassword/$
    return render(request, 'user/forgetpassword.html')


# 账户余额
@check_login
def records(request):  # ^records/$
    return render(request, 'user/records.html')


# 积分
@check_login
def integral(request):  # ^integral/$
    return render(request, 'user/integral.html')


# 积分兑换
@check_login
def integralexchange(request):  # ^integralexchange/$
    return render(request, 'user/integralexchange.html')


# 兑换记录
@check_login
def integralrecords(request):  # ^integralrecords/$
    return render(request, 'user/integralrecords.html')


# 优惠券
@check_login
def yhq(request):  # ^yhq/$
    return render(request, 'user/yhq.html')


# 已过期
@check_login
def ygq(request):  # ^ygq/$
    return render(request, 'user/ygq.html')


# 我的收藏
@check_login
def collect(request):  # ^collect/$
    return render(request, 'user/collect.html')


# 编辑收藏
@check_login
def collect_edit(request):  # ^collect_edit/$
    return render(request, 'user/collect-edit.html')


# 个人资料
@check_login
def infor(request):  # ^infor/$
    return render(request, 'user/infor.html')


# 收货地址
@check_login
def gladdress(request):  # ^gladdress/$
    return render(request, 'user/gladdress.html')


# 安全设置
@check_login
def saftystep(request):  # ^saftystep/$
    return render(request, 'user/saftystep.html')


# 我的钱包
@check_login
def money(request):  # ^money/$
    return render(request, 'user/money.html')


# 我要兼职
@check_login
def job(request):  # ^job/$
    return render(request, 'user/job.html')


# 推荐有奖
@check_login
def recommend(request):  # ^recommend/$
    return render(request, 'user/recommend.html')


# 我的推荐
@check_login
def myrecommend(request):  # ^myrecommend/$
    return render(request, 'user/myrecommend.html')


# 我的动态
@check_login
def message(request):  # ^message/$
    return render(request, 'user/message.html')


# 发布动态
@check_login
def release(request):  # ^release/$
    return render(request, 'user/release.html')


# 系统设置
@check_login
def step(request):  # ^step/$
    return render(request, 'user/step.html')


# 关于我们
@check_login
def about(request):  # ^about/$
    return render(request, 'user/about.html')
