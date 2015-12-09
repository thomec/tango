# lists/views.py


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError

from lists.models import Item, List
from lists.forms import ItemForm, ExistingListItemForm


def home_page(request):
    return render(request, 'lists/home.html', {'form': ItemForm()})


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        # Item.objects.create(text=request.POST['text'], list=list_)
        form.save(for_list=list_)   # using the form.save() method instead of objects.create()
        return redirect(list_)      # using get_absolute_url instead of ('view_list', list_.id)
    else:
        return render(request, 'lists/home.html', {'form': form})


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)

    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)      # instead of ('/lists/%d/' % (list_.id,))

    return render(request, 'lists/list.html', {'list': list_, 'form': form})



