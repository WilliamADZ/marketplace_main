from django.shortcuts import render
from .models import Item, category
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    items = Item.objects.filter(is_sold=False)
    categories = category.objects.all()

    context  = {
    'items': items,
    'categories': categories
    }
    return render(request, 'store/home.html', context)