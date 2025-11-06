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

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.Category,is_sold=False).exclude(pk=pk)[0:3]


    context={
        'item': item,
        'related_items': related_items
    }

    return render(request, 'store/items.html', context)