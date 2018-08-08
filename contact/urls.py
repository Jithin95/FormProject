from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name= 'contact_index'),
    path('form/', views.indexforms, name= 'contact_index_form'),
    path('formview/', views.ContactForm.as_view(), name= 'formview'),

]
