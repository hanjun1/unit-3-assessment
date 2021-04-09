from django.shortcuts import render, redirect
from .models import WackyWidget
# Create your views here.


def index(request):
    widget_list = WackyWidget.objects.all()
    if len(widget_list) > 0:
        widget_quantity_total = 0
        for widget in widget_list:
            widget_quantity_total += widget.quantity
    context = {
        'widget_list': widget_list,
        'widget_quantity_total': widget_quantity_total,
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == "POST":
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')
        WackyWidget.objects.create(description=description, quantity=quantity)
    return redirect('index')


def delete(request, widget_id):
    widget = WackyWidget.objects.get(id=widget_id)
    widget.delete()
    return redirect('index')
