from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, CreateView, DetailView)
from django.contrib import messages
from django.urls import reverse



from .models import Author, Book


class HomeView(TemplateView):
    template_name = 'home.html'


class AuthorsView(ListView):
    model = Author
    template_name = 'author_list.html'


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'author_create.html'
    fields = ['name',]

    def form_valid(self, form):
        
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The author has been added'
        )

        return super().form_valid(form)


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'






