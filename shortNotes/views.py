from django.shortcuts import render
from django.views.generic.list import ListView
from .models import ShortNotes, ShortNotesType, ShortNotesModuleType
from django.views.generic.base import TemplateView


class ShortNotesListView(TemplateView):
    template_name = "shortnotes/list.html"

    def get_context_data(self, **kwargs):
        context = super(ShortNotesListView, self).get_context_data(**kwargs)
        context["type_list"] = ShortNotesType.objects.all()
        context["module_list"] = ShortNotesModuleType.objects.all()
        context["object_list"] = ShortNotes.objects.all().order_by("-id")
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        post_dict = request.POST
        obj = ShortNotes()
        obj.title = post_dict['title']
        obj.content_type = ShortNotesType.objects.get(id=int(post_dict['typeName']))
        obj.module_type = ShortNotesModuleType.objects.get(id=int(post_dict['moduleName']))
        obj.content = post_dict['content']
        obj.save()
        return self.render_to_response(context)