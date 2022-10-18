from django.urls import path

from projectApp.models import MyView
#now import the views.py file into this code
from . import views
from django.contrib import admin
from .views import GeeksCreate, GeeksDeleteView, GeeksDetailView, GeeksFormView, GeeksList, GeeksUpdateView, create_view, delete_view, geeks_view, list_view,detail_view, update_view

urlpatterns=[
  path('admin/', admin.site.urls),
  # path('',views.home_view)
  # path('',views.formset_view),
  # path('', geeks_view),
  # path('', list_view),
  path('', create_view),

  path('<id>', detail_view),
  path('<id>/update', update_view),
  path('<id>/delete', delete_view ),
  path('about/', MyView.as_view()),
  # path('', GeeksCreate.as_view() ),
  # path('', GeeksList.as_view()),
  path('<pk>/', GeeksDetailView.as_view()),
  path('<pk>/update', GeeksUpdateView.as_view()),
  path('<pk>/delete/', GeeksDeleteView.as_view()),
  # path('', GeeksFormView.as_view()),

]