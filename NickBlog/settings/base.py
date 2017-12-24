"""
Django settings for NickBlog project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7zbpqsg*2z5gz8s32!#6-72tw$_n55j12io4#kzttye29_(uu7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = (
    # django-suit Admin界面美化插件
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    # 'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # django-haystack 全局搜索插件
    'haystack',
    'article',
    # DjangoUeditor 富文本编辑器插件
    'DjangoUeditor',
    # dj-pagination 自动分页插件
    'dj_pagination',
    # django-silk http请求和sql查询分析插件
    'silk',
    'account',
)

# 扩展AbstractUser模型，构建新的account应用需要的配置
AUTH_USER_MODEL = 'account.Account'
# 不记录跳转来的页面，登陆/注销后直接回到上一个页面
LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/account/login/'
LOGOUT_URL = '/account/logout/'
# 设置模拟发送邮件到终端（对于数据库中有的邮箱地址）
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# 添加自定义用户邮件验证后端
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'account.backends.EmailBackend',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # 分页中间件
    'dj_pagination.middleware.PaginationMiddleware',
    # 请求分析中间件
    'silk.middleware.SilkyMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    # 启用dj-paginate
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    # django-suit Admin界面美化
    "django.core.context_processors.request",
)

ROOT_URLCONF = 'NickBlog.urls'

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
            ],
        },
    },
]

# 设置缓存后端：使用MemcachedCache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        # 缓存过期时间
        'TIMEOUT': 60,
        # 可选项
        'OPTIONS': {
            # 缓存允许的最大条目数
            'MAX_ENTRIES': 100,
            # 达到 MAX_ENTRIES 的时候,被删除的条目比率 1/MAX_ENTRIES
            'CULL_FREQUENCY': 2,
        }
    }
}

WSGI_APPLICATION = 'NickBlog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# MySQL数据库配置项
MYSQL_OPTIONS = {
    # 使用严格模式TRADITIONAL插入数据
    'sql_mode': 'TRADITIONAL',
    'charset': 'utf8',
    # 连接到数据库时会执行init_command对应的命令，创建表之后就即可删除此选项
    'init_command': """
    SET default_storage_engine=INNODB;
    SET character_set_connection=utf8,collation_connection=utf8_unicode_ci;
    SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
    """
}
# MySQL数据库引擎
DATABASES = {
    'default': {
        # 事务回调API transaction_hooks
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'NickBlog',
        'USER': os.environ.get('DATABASE_USER', 'root'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'password') or None,
        'HOST': os.environ.get('DATABASE_HOST', '127.0.0.1'),
        'PORT': os.environ.get('DATABASE_PORT', 3306),
        # 指定数据库配置
        'OPTIONS': MYSQL_OPTIONS,
        # 设置数据库交互方式为事务
        'ATOMIC_REQUESTS': True,
        'TEST': {
            'NAME': 'test_ralph_ng',
        }
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = './var/www/NickBlog/static/'

# 公共的static文件
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "static/media"),
)

# upload floder
MEDIA_URL = '/static/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')

STATICFILES_FINDERS = ("django.contrib.staticfiles.finders.FileSystemFinder",
                       "django.contrib.staticfiles.finders.AppDirectoriesFinder",)


# @@@@@@@@@第三方插件配置@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# 分页插件 无效页面抛出404错误
PAGINATION_INVALID_PAGE_RAISES_404 = True

# 搜索设置
HAYSTACK_CONNECTIONS = {
    'default': {
        # 'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'ENGINE': 'article.whoosh_cn_backend.WhooshEngine',
        # 注意这个路径，路径错了就无法生成索引！
        'PATH': os.path.join(os.path.dirname(os.path.dirname(__file__)), 'whoosh_index'),
    },
}
# 设置搜索结果每页多少条
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 8
# 设置信号处理器
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# silk cprofile文件配置
# SILKY_PYTHON_PROFILER = True
# SILKY_PYTHON_PROFILER_BINARY = True
# SILKY_STORAGE_CLASS = 'silk.storage.ProfilerResultStorage'
# SILKY_PYTHON_PROFILER_RESULT_PATH = os.path.join(BASE_DIR, 'static/profiling')
# 必须登陆才能访问silk
SILKY_AUTHENTICATION = True  # User must login
SILKY_AUTHORISATION = True  # User must have permissions

# suit界面配置
# Django Suit configuration example
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Nick CMS',
    # 左上角时间显示设置 https://docs.djangoproject.com/en/dev/ref/templates/builtins/#std:templatefilter-date
    'HEADER_DATE_FORMAT': 'Y-m-j l',
    'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 自动将星号符号添加*到每个必填字段标签的末尾
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 离开未保存的表单时会提醒,设置为False则不会保存就离开
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    'MENU_ICONS': {
       'sites': 'icon-leaf',
       'auth': 'icon-lock',
    },
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 排除某个app和model
    # 'MENU_EXCLUDE': ('auth.group',),
    # 使用自定义菜单 针对左侧栏位
    'MENU': (
        'sites',
        {'app': 'article', 'icon': 'icon-star', 'label': '文章'},
        {'app': 'account', 'icon': 'icon-lock', 'label': '用户'},
        {'app': 'auth', 'icon': 'icon-cog', 'label': '用户组', 'models': ('auth.group', )},

    ),
    # misc
    # 每页列出多少条 指定所有模型的列出
    # 'LIST_PER_PAGE': 15,
}