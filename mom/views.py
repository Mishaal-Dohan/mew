
from django.urls import reverse_lazy
from .models import Dog, DogHome
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.shortcuts import render
from django.http import Http404
# Create your views here.


class DogListView(ListView):
    model = Dog
    template_name = 'dog_list.html'
    context_object_name = 'all_dogs_list'


class DogDetailView(DetailView):
    model = Dog
    template_name = 'dog_detail.html'


class DogUpdateView(UpdateView):
    model = Dog
    template_name = 'dog_edit.html'
    fields = ['home']


class DogDeleteView(DeleteView):
    model = Dog
    template_name = 'dog_delete.html'
    success_url = reverse_lazy('dog_list')


def query1(requst):
    try:
        dogs_list = Dog.objects.filter(home_name='CanineCare')
    except Dog.DoesNotExist:
        raise Http404("Dog dose not exist")
    return render(requst, 'db_query1.html', {'dogs': dogs_list, })


def query2(requst):
    try:
        number = Dog.objects.filter(home_name='PupMotel')
    except Dog.DoesNotExist:
        raise Http404("Dog dose not exist")
    return render(requst, 'db_query2.html', {'num': number, })


def query3(requst):
    try:
        dog = Dog.objects.earliest('arrval_date')
    except Dog.DoesNotExist:
        raise Http404("Dog dose not exist")
    return render(requst, 'db_query3.html', {'name': dog.name, })


def query4(requst):
    try:
        dog = Dog.objects.earliest('date_of_birth')
    except Dog.DoesNotExist:
        raise Http404("Dog dose not exist")
    return render(requst, 'db_query4.html', {'name': dog.name, })


def query5(requst):
    try:
        num = DogHome.objects.all().count()
    except Dog.DoesNotExist:
        raise Http404("Dog dose not exist")
    return render(requst, 'db_query5.html', {'number': num, })


def query6(requst):
    try:
        sorted_list = Dog.objects.order_by('name')
    except Dog.DoesNotExist:
        raise Http404("Dog dose not exist")
    return render(requst, 'db_query6.html', {'slist': sorted_list, })


def query7(requst):
    try:
        number = Dog.objects.filter(breed='Crossbrees').count()
    except Dog.DoesNotExist:
        raise Http404("Dog dose not exist")
    return render(requst, 'db_query7.html', {'num': number, })
