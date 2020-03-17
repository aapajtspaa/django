from django.urls import path, include
from . import views

app_name = 'todolist'
urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='主页'),
    path('about/', views.about, name='关于'),
    path('form/<forloop_counter>', views.form, name='编辑'),
    path('del/<forloop_counter>', views.delete, name='删除'),
    path('form/', views.form, name='编辑'),
    path('cross/<forloop_counter>', views.cross, name='完成'),
]
