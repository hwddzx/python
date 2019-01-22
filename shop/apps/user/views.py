import random
import uuid

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
import re
from django_redis import get_redis_connection

from user import set_password
from user.forms import UsersForm, LoginForm, InforForm, PasswordForm
from user.helps import check_login, send_sms
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
def forgetpassword(request):  # ^forgetpassword/$
    return render(request, 'user/forgetpassword.html')


# 发送短信验证码
class SendMsg(View):
    def get(self, requset):
        pass

    def post(self, requset):
        # 1接收参数
        telephone = requset.POST.get("telephone", '')
        rs = re.search('^1[3-9]\d{9}$', telephone)
        # 判断参数合法性
        if rs is None:
            return JsonResponse({'error': 1, 'errmsg': '电话号码格式错误'})
        # 2处理数据
        # 模拟,最后接入运营商
        """
            1.生成随机验证码
            2.保存验证码 保存到Redis中,存取速度快,方便设置有效时间
            3.接入运营商
       """
        # 生成随机验证码字符串
        random_code = "".join([str(random.randint(0, 9)) for _ in range(6)])
        print("==========={}=============".format(random_code))
        # 保存验证码到redis
        # 获取连接
        r = get_redis_connection()
        # 保存手机号码对应的验证码
        r.set(telephone, random_code)
        r.expire(telephone, 60)  # 设置60s后过期
        # 首先获取当前手机号码的发送次数
        key_times = "{}_times".format(telephone)
        now_times = r.get(key_times)  # 从redis获取的是二进制,需要转换
        # now_times = now_times.decode('utf-8')
        # now_times = int(now_times)
        if now_times is None or int(now_times) < 100:
            # 保存手机发送验证码的次数,不能超过5次
            r.incr(key_times)
            # 设置过期时间
            r.expire(key_times, 3600)
        else:
            # 返回,告诉用户发送次数过多
            return JsonResponse({'error': 1, "errmsg": "发送次数过多"})

        # 接入运营商
        # >>>3. 接入运营商
        __business_id = uuid.uuid1()
        params = "{\"code\":\"%s\",\"product\":\"嘟狗宠物店\"}" % random_code
        # params = "{\"code\":\"我爱你\",\"product\":\"嘟狗宠物店\"}"
        # print(params)
        rs = send_sms(__business_id, telephone, "注册验证", "SMS_2245271", params)
        print(rs.decode('utf-8'))

        # 3合成响应
        return JsonResponse({'error': 0})


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
class InforView(View):
    @method_decorator(check_login)
    def get(self, request):
        # 回显个人资料
        # 根据session中保存的ID查询数据库
        telephone = request.session.get('ID')
        data = User.objects.get(telephone=telephone)
        context = {
            "data": data
        }
        return render(request, 'user/infor.html', context=context)

    @method_decorator(check_login)
    def post(self, request):
        # 接收参数
        data = request.POST
        form = InforForm(data)
        # 判断合法性
        if form.is_valid():
            # 合法
            phone = request.session.get('ID')
            username = data['username']
            gender = data['gender']
            birthday = data['birthday']
            school = data['school']
            hometown = data['hometown']
            location = data['location']
            telephone = data['telephone']
            # 修改数据库
            User.objects.filter(telephone=phone).update(username=username, birthday=birthday, school=school,
                                                        hometown=hometown, location=location, gender=gender,
                                                        telephone=telephone)
            # 重新创建session
            request.session['ID'] = telephone
            return redirect('user:个人中心')
        else:
            # 不合法
            # 返回错误提示
            errors = form.errors
            return render(request, 'user/infor.html', context=errors)


# 收货地址
@check_login
def gladdress(request):  # ^gladdress/$
    return render(request, 'user/gladdress.html')


# 安全设置
@check_login
def saftystep(request):  # ^saftystep/$
    return render(request, 'user/saftystep.html')


# 修改密码
class PasswordView(View):
    @method_decorator(check_login)
    def get(self, request):
        return render(request, 'user/password.html')

    @method_decorator(check_login)
    def post(self, request):
        # 接收参数
        data = request.POST
        form = PasswordForm(data)
        if form.is_valid():
            # 合法
            # 将密码加密
            new_password = set_password(form.cleaned_data.get('password1'))
            # 修改数据库中密码
            User.objects.filter(telephone=form.cleaned_data.get('telephone')).update(password=new_password)
            # 密码修改成功,清楚session并返回登录界面
            request.session.flush()
            return redirect('user:登录')
        else:
            errors = form.errors
            return render(request, 'user/password.html', context=errors)


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


# 绑定手机
@check_login
def boundphone(request):  # ^boundphone/$
    return render(request, 'user/boundphone.html')


# 关于我们
@check_login
def about(request):  # ^about/$
    return render(request, 'user/about.html')


# 设置支付密码
@check_login
def payment(request):  # ^payment/$
    return render(request, 'user/payment.html')


# 申请兼职
@check_login
def applicationjob(request):  # ^applicationjob/$
    return render(request, 'user/applicationjob.html')


# 申请记录
@check_login
def application(request):  # ^application/$
    return render(request, 'user/application.html')


# 安全退出
@check_login
def sign_out(request):
    request.session.flush()
    return redirect('user:登录')
