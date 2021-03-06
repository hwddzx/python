import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=83#wm^k52rg234hrr#+ui9zw(gol+(zc3xsru(g222+qi63bn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # 上线改为False

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haystack',  # 全文检索框架
    # 添加子应用
    'user.apps.UserConfig',
    'order.apps.OrderConfig',
    'shopping_cart.apps.ShoppingCartConfig',
    'commodity.apps.CommodityConfig',
    'ckeditor',  # 添加ckeditor富文本编辑器
    'ckeditor_uploader',  # 添加ckeditor富文本编辑器文件上传部件
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'shop.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

# 设置时区
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# 设置静态文件根目录  上线的时候使用一次
# STATIC_ROOT = os.path.join(BASE_DIR, "static")

# 添加django中的缓存配置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",  # redis启动起来, 使用的1号数据库 (0-15)
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# 修改默认sessioin的存储引擎
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# 配置短信需要的key
ACCESS_KEY_ID = "LTAI2qSiJdWP87em"
ACCESS_KEY_SECRET = "FzORQ587PgGBoOAdmxzCjaxQi8klUi"

# 分配一个资源URL
MEDIA_URL = "/static/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')

# 设置ckeditor的上传目录
CKEDITOR_UPLOAD_PATH = "uploads/"

# 编辑器样式配置
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}

# 全文检索框架的配置
HAYSTACK_CONNECTIONS = {
    'default': {
        # 配置搜索引擎 修改成自己配置的搜索引擎
        'ENGINE': 'utils.whoosh_cn_backend.WhooshEngine',
        # 配置索引文件目录
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}
# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
# 每页显示条数
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 50

"""
# 七牛云密钥等配置
QINIU_ACCESS_KEY = 'eCWAJaH6vmFJYN3OHgVOnuwXFabov0XlkEiNbkuc'
QINIU_SECRET_KEY = 'mOCiBdX_zRQ1FGBq8_rAxhdTJzsDw6nP4Ld0052X'
QINIU_BUCKET_NAME = 'image-shop'
QINIU_BUCKET_DOMAIN = 'pmzxu7b75.bkt.clouddn.com'
QINIU_SECURE_URL = False  # 使用http
PREFIX_URL = 'http://'

# 上传文件地址配置
MEDIA_URL = PREFIX_URL + QINIU_BUCKET_DOMAIN + "/"
# 上传文件的存储引擎配置
DEFAULT_FILE_STORAGE = 'qiniustorage.backends.QiniuStorage'

# 静态文件的url配置
STATIC_URL = QINIU_BUCKET_DOMAIN + '/static/'
# 静态文件的存储引擎
STATICFILES_STORAGE = 'qiniustorage.backends.QiniuStaticStorage'  # 七牛云配置结束
"""
