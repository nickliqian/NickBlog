from haystack.views import SearchView


# 自定义搜索视图
class MySearchView(SearchView):
    # 重载extra_context来添加额外的context内容
    def extra_context(self):
        context = super(MySearchView, self).extra_context()
        context['side_list'] = 'side_list'
        return context
