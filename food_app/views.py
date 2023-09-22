#django
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# models
from food_app.models import Food_Item


# Create your views here.
def index(request):
    food_list = Food_Item.objects.all()
    template = 'index.html'
    # creates a dictonary of food_items
    context = {
        'food_list' : food_list
    }
    # one way to render templates
    # return HttpResponse(template.render(context, request))
    return render(request, template, context)

def details(request, item_id):
    template = 'details.html'
    # creates a dictonary of food_items

    item_id = Food_Item.objects.get(pk= item_id)
    print(item_id)
    context = {
        'food_item': item_id
    }
    return render(request, template, context)

def edit(request, item_id):
    template = 'edit_item.html'
    # creates a dictonary of food_items

    item_id = Food_Item.objects.get(id = item_id)
    print(item_id)
    context = {
        'food_item': item_id
    }
    return render(request, template, context)