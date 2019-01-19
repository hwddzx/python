from django.shortcuts import render


# 个人中心
def member(request):  # ^$
    return render(request, 'user/member.html')


# 登陆
def login(request):  # ^login/$
    return render(request, 'user/login.html')


# 注册
def reg(request):  # ^reg/$
    return render(request, 'user/reg.html')


# 忘记密码
def forgetpassword(request):  # ^forgetpassword/$
    return render(request, 'user/forgetpassword.html')


# 账户余额
def records(request):  # ^records/$
    return render(request, 'user/records.html')


# 积分
def integral(request):  # ^integral/$
    return render(request, 'user/integral.html')


# 积分兑换
def integralexchange(request):  # ^integralexchange/$
    return render(request, 'user/integralexchange.html')


# 兑换记录
def integralrecords(request):  # ^integralrecords/$
    return render(request, 'user/integralrecords.html')


# 优惠券
def yhq(request):  # ^yhq/$
    return render(request, 'user/yhq.html')


# 已过期
def ygq(request):  # ^ygq/$
    return render(request, 'user/ygq.html')


# 我的收藏
def collect(request):  # ^collect/$
    return render(request, 'user/collect.html')


# 编辑收藏
def collect_edit(request):  # ^collect_edit/$
    return render(request, 'user/collect-edit.html')


# 个人资料
def infor(request):  # ^infor/$
    return render(request, 'user/infor.html')


# 收货地址
def gladdress(request):  # ^gladdress/$
    return render(request, 'user/gladdress.html')


# 安全设置
def saftystep(request):  # ^saftystep/$
    return render(request, 'user/saftystep.html')


# 我的钱包
def money(request):  # ^money/$
    return render(request, 'user/money.html')


# 我要兼职
def job(request):  # ^job/$
    return render(request, 'user/job.html')


# 推荐有奖
def recommend(request):  # ^recommend/$
    return render(request, 'user/recommend.html')


# 我的推荐
def myrecommend(request):  # ^myrecommend/$
    return render(request, 'user/myrecommend.html')


# 我的动态
def message(request):  # ^message/$
    return render(request, 'user/message.html')


# 系统设置
def step(request):  # ^step/$
    return render(request, 'user/step.html')


# 关于我们
def about(request):  # ^about/$
    return render(request, 'user/about.html')
