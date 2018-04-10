from django.shortcuts import render
from django.views.generic.list import ListView
from .models import ShortNotes, ShortNotesType


class ShortNotesListView(ListView):
    model = ShortNotes
    template_name = "shortnotes/list.html"

    def get_context_data(self, **kwargs):
        context = super(ShortNotesListView, self).get_context_data(**kwargs)
        return context