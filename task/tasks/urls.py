"""Определяет схемы URL для task."""

from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Страница со списком всех тем.
    path('tasks/', views.tasks, name='tasks'),
    # Страница с подробной информацией по отдельной теме
    path('tasks/<int:task_id>/', views.task, name='task'),
    # Страница для добавления новой темы
    path('new_task/', views.new_task, name='new_task'),
    # Страница для добавления новой записи
    path('new_entry/<int:task_id>/', views.new_entry, name='new_entry'),
    # Страница для редактирования записи
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
