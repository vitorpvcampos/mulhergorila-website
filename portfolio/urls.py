from django.urls import path

from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('projeto/<slug:slug>', views.portfolio_detail, name='portfolio_detail'),
]
