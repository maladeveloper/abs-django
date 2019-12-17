from django.shortcuts import render
from django.http import HttpResponse
from .models import abs_immigration
# from .forms import abs_immigration_form
from .forms import RawImmigrationForm
from django.shortcuts import get_object_or_404
import pandas as pd
from .ABS_migration import process_immigration_per_year
import os

from plotly.offline import plot
from plotly.graph_objs import Scatter


# Create your views here.
#
# def abs_form_create_view(request):
#     form= abs_immigration_form(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form=abs_immigration_form()
#     context = {
#         "form": form
#     }
#     return render(request, "user_data.html", context)


def abs_form_create_view(request):
    print(request.method)
    form= RawImmigrationForm()
    if request.method== "POST":
        form= RawImmigrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            abs_immigration.objects.create(**form.cleaned_data)
            obj_to_send= abs_immigration.objects.latest('pub_date')
            return process_data(obj_to_send,request)

        else:
            print(form.errors)
    context={
        "form":form
    }
    return render(request, "user_data.html", context)


def secondary_immigration_detail_view(request):
    obj= abs_immigration.objects.get(id=1)
    context= {
        "obj": obj
    }
    return render(request, "data.html",context)

def dynamic_lookup_view(request,my_id):
    obj= get_object_or_404(abs_immigration,id=my_id)
    context={
        "obj": obj
    }
    return render(request,"data.html",context)

def abs_immigration_list_view(request):
    print(request.method)
    print(request)
    array_obj=[]
    for e in abs_immigration.objects.all():
        array_obj.append(e)
    array_obj.reverse()
    context={
        "obj":array_obj
    }
    return render(request,"list_data.html ",context)

def process_data(obj,request):
    framed_data= pd.read_csv(os.getcwd()+"/abs_immigration/net_immigration_data.csv")
    gender= obj.gender
    region=obj.region
    measure= int(obj.migration_type)
    data_array=process_immigration_per_year(framed_data,gender,region,measure)
    x_data=data_array[0]
    y_data=data_array[1]
    plot_div = plot([Scatter(x=x_data, y=y_data,
                             mode='lines', name='test',
                             opacity=0.8, marker_color='green')],
                    output_type='div')
    context={
        "plot_div":plot_div
    }
    return render(request,"process_data.html",context)
