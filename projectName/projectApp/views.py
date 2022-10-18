from django.shortcuts import render
from .forms import InputForm
from .forms import GeeksForm
from .models import GeeksModel
 
# Create your views here.
# def home_view(request):
#     context ={}
 
#     # create object of form
#     form = GeeksForm(request.POST or None, request.FILES or None)
     
#     # check if form data is valid
#     if form.is_valid():
#         # save the form data to model
#         form.save()
 
#     context['form']= form
#     return render(request, "home.html", context)


from django.shortcuts import render
  
# relative import of forms
from .forms import GeeksForm
  
# importing formset_factory
from django.forms import formset_factory


from django.shortcuts import render
from .forms import GeeksForm
 
def home_view(request):
    context ={}
 
    # create object of form
    form = GeeksForm(request.POST or None, request.FILES or None)
     
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
 
    context['form']= form
    return render(request, "home.html", context)

  
# def formset_view(request):
#     context ={}
  
#     # creating a formset
#     GeeksFormSet = formset_factory(GeeksForm)
#     formset = GeeksFormSet()
      
#     # Add the formset to context dictionary
#     context['formset']= formset
#     return render(request, "home.html", context)




# def formset_view(request):
#     context ={}
  
#     # creating a formset and 5 instances of GeeksForm
#     GeeksFormSet = formset_factory(GeeksForm, extra = 5)
#     formset = GeeksFormSet()
      
#     # Add the formset to context dictionary
#     context['formset']= formset
#     return render(request, "home.html", context)



from django.shortcuts import render
  
# relative import of forms
from .forms import GeeksForm
  
# importing formset_factory
from django.forms import formset_factory
  
def formset_view(request):
    context ={}
  
    # creating a formset and 5 instances of GeeksForm
    GeeksFormSet = formset_factory(GeeksForm, extra = 3)
    formset = GeeksFormSet(request.POST or None)
      
    # print formset data if it is valid
    if formset.is_valid():
        for form in formset:
            print(form.cleaned_data)
              
    # Add the formset to context dictionary
    context['formset']= formset
    return render(request, "home.html", context)



    # import Http Response from django
from django.shortcuts import render
  
# # create a function
# def geeks_view(request):
#     # create a dictionary to pass
#     # data to the template
#     context ={
#         "data":"Gfg is the best",
#         "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     }
#     # return response with template and context
#     return render(request, "geeks.html", context)










    # import Http Response from django
from django.http import HttpResponse
# get datetime
import datetime
 
# create a function
def geeks_view(request):
    # fetch date and time
    now = datetime.datetime.now()
    # convert to string
    html = "Time is {}".format(now)
    # return response
    return HttpResponse(html)





from django.shortcuts import render
 
# relative import of forms
from .models import GeeksModel
 
 
def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = GeeksModel.objects.all()
         
    return render(request, "list_view.html", context)








    from django.shortcuts import render
 
# relative import of forms
from .models import GeeksModel
from .forms import GeeksForm
 
 
def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "create_view.html", context)



from django.shortcuts import render
 
# relative import of forms
from .models import GeeksModel
 
# pass id attribute from urls
def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = GeeksModel.objects.get(id = id)
         
    return render(request, "detail_view.html", context)




from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
 
# relative import of forms
from .models import GeeksModel
from .forms import GeeksForm
 
# after updating it will redirect to detail_View
def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
  
    # add the dictionary during initialization
    context["data"] = GeeksModel.objects.get(id = id)
          
    return render(request, "detail_view.html", context)
 
# update view for details
def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id = id)
 
    # pass the object as instance in form
    form = GeeksForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_view.html", context)





from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
 
from .models import GeeksModel
 
 
# delete view for details
def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "delete_view.html", context) 





from django.http import HttpResponse
from django.views import View 
def my_view(request):
    if request.method == 'GET':
        # <view logic>
        return HttpResponse('result')  






from django.views.generic.edit import CreateView
from .models import GeeksModel
 
class GeeksCreate(CreateView):
 
    # specify the model for create view
    model = GeeksModel
 
    # specify the fields to be displayed
 
    fields = ['title', 'description']

from django.views.generic.list import ListView
from .models import GeeksModel
 
class GeeksList(ListView):
 
    # specify the model for list view
    model = GeeksModel

from django.views.generic.detail import DetailView
 
from .models import GeeksModel
 
class GeeksDetailView(DetailView):
    # specify the model to use
    model = GeeksModel

from django.views.generic.edit import UpdateView
 
# Relative import of GeeksModel
from .models import GeeksModel
 
class GeeksUpdateView(UpdateView):
    # specify the model you want to use
    model = GeeksModel
 
    # specify the fields
    fields = [
        "title",
        "description"
    ]
 
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url ="/"



# import generic UpdateView
from django.views.generic.edit import DeleteView
 
# Relative import of GeeksModel
from .models import GeeksModel
 
class GeeksDeleteView(DeleteView):
    # specify the model you want to use
    model = GeeksModel
     
    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url ="/"



# import generic FormView
from django.views.generic.edit import FormView
 
# Relative import of GeeksForm
from .forms import GeeksForm
 
class GeeksFormView(FormView):
    # specify the Form you want to use
    form_class = GeeksForm
     
    # specify name of template
    template_name = "geeks / geeksmodel_form.html"
 
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url ="/thanks/"

