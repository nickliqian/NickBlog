from NickBlog.settings.base import *
import six

DEBUG = True

# 添加调试工具和扩展工具
INSTALLED_APPS = INSTALLED_APPS + (
    'debug_toolbar.apps.DebugToolbarConfig',
    'django_extensions',
)

# @@@@@@@@@第三方插件配置@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# 开发环境下任何用户都有访问silk的权限
SILKY_AUTHENTICATION = False  # User must login
SILKY_AUTHORISATION = False  # User must have permissions


# debug_toolbar 配置
DEBUG_TOOLBAR_PATCH_SETTINGS = False

# 添加调试工具中间件
MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# 使用调试工具的IP
INTERNAL_IPS = ("127.0.0.1",)

# debug_toolbar 配置项
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]

CONFIG_DEFAULTS = {
    # Toolbar options
    'DISABLE_PANELS': {'debug_toolbar.panels.redirects.RedirectsPanel'},
    'INSERT_BEFORE': '</body>',
    'JQUERY_URL': '//cdn.bootcss.com/jquery/2.1.4/jquery.min.js',
    'RENDER_PANELS': None,
    'RESULTS_CACHE_SIZE': 10,
    'ROOT_TAG_EXTRA_ATTRS': '',
    'SHOW_COLLAPSED': False,
    'SHOW_TOOLBAR_CALLBACK': 'debug_toolbar.middleware.show_toolbar',
    # Panel options
    'EXTRA_SIGNALS': [],
    'ENABLE_STACKTRACES': True,
    'HIDE_IN_STACKTRACES': (
        'socketserver' if six.PY3 else 'SocketServer',
        'threading',
        'wsgiref',
        'debug_toolbar',
        'django',
    ),
    'PROFILER_MAX_DEPTH': 10,
    'SHOW_TEMPLATE_CONTEXT': True,
    'SKIP_TEMPLATE_PREFIXES': (
        'django/forms/widgets/',
        'admin/widgets/',
    ),
    'SQL_WARNING_THRESHOLD': 500,   # milliseconds
}
