from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Things

class ThingsListView(ListView):
    template_name = "things/things-list.html"
    model = Things


class ThingsDetailView(DetailView):
    template_name = "things/things-detail.html"
    model = Things


class ThingsCreateView(CreateView):
    template_name = "things/things-create.html"
    model = Things
    fields = ['name', 'description', 'owner']


class ThingsUpdateView(UpdateView):
    template_name = "things/things-update.html"
    model = Things
    fields = ['name', 'description', 'owner']


class ThingsDeleteView(DeleteView):
    template_name = "things/things-delete.html"
    model = Things
    success_url = reverse_lazy("things_list")