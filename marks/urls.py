from django.urls import path
from .views import marks_list, marks_add

urlpatterns = [
    path("", marks_list, name="marks_list"),
    path("add/", marks_add, name="marks_add"),
]
