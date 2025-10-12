from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .forms import GeeksForm
from .models import Geekmodels
from django.views.generic.list import ListView

# Create your views here
def create_view(request):
    context = {}

    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context['form'] = form
    return render(request, "create_view.html", context)


def list_view(request):
    context = {}

    # list view
    context['dataset'] = Geekmodels.objects.all()

    return render(request, "list_view.html", context)

def detail_view(request, id):
    context = {}

    context['data'] = Geekmodels.objects.get(id=id)
    return render(request, "detail_view.html", context)

def update_view(request, id):
    context = {}

    obj = get_object_or_404(Geekmodels, id=id)

    form = GeeksForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+str(id))
    context["form"] = form
    return render(request, "update_view.html", context)

def delete_view(request, id):
    context = {}

    obj = get_object_or_404(Geekmodels, id=id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)
class GeeksList(ListView):
    model = Geekmodels