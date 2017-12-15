from NickBlog.settings.base import *


DEBUG = True

# 添加调试工具和扩展工具
INSTALLED_APPS = INSTALLED_APPS + (
    'debug_toolbar',
    'django_extensions',
)

# 添加调试工具中间件
MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# 使用调试工具的IP
INTERNAL_IPS = ("127.0.0.1",)

# debug_toolbar 配置项
