from django.urls import path

from . import views

urlpatterns = [
    path('',views.add_show, name = "addandshow"),
    path('delete/<int:id>',views.delete, name = "delete"),
    path('update/<int:id>',views.update, name = "update"),
]