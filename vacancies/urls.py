"""stepik_find URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from vacancies.views import MainView, CompanyView, VacanciesListView, VacanciesCatView, VacancyView

urlpatterns = [
    path('', MainView.as_view(), name='main-view'),
    path('vacancies/', VacanciesListView.as_view(), name='vacancies-view'),
    path('vacancies/cat/<str:category>', VacanciesCatView.as_view(), name='vacancies-cat-view'),
    path('vacancies/<int:id>', VacancyView.as_view(), name='vacancies-id-view'),
    path('companies/<int:id>', CompanyView.as_view(), name='companies-view'),
]
