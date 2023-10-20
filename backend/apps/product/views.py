from django.shortcuts import render
from django.views.generic import TemplateView
from django_filters.views import FilterView
from .models import Car
from .filters import CarFilter


class ProductView(FilterView):
    model = Car
    template_name = 'index.html'
    filterset_class = CarFilter









