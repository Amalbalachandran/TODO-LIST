from . import views
from django.contrib import admin
from django.urls import path
app_name = 'fapp'

urlpatterns = [
    path('',views.home,name='home'),
    path('insert/',views.insert,name='insert'),
    path('edit_task/<int:todo_id>/',views.edit,name='edit'),
    path('update_task/<int:todo_id>/',views.update,name='update'),
    path('insert_task/<int:id>/',views.insert,name='insert'),
    path('delete/<int:id>/',views.delete,name='delete')
]