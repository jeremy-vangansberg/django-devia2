from django.shortcuts import render
from .models import Functionnality
from django.views.generic import ListView

class FunctionalityListView(ListView):
    model = Functionnality
    template_name = "functionnalities/func_list.html"
    context_object_name = "func_list"

