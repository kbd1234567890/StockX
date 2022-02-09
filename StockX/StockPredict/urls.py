
from django.urls import path

from . import views

urlpatterns = [

    path('', views.dashboard),
    path('document', views.document),
    path('table', views.companyList),
    path('about', views.about)
]