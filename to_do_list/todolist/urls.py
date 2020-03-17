from django.urls import path, include
from . import views

app_name = 'todolist'
urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='主页'),
    path('about/', views.about, name='关于'),
    path('form/<thing_id>', views.form, name='编辑'),
    path('del/<thing_id>', views.delete, name='删除'),
    path('form/', views.form, name='编辑'),
    path('cross/<thing_id>', views.cross, name='完成'),
]
