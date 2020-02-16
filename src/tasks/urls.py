from django.urls import include, path
from .views import *

urlpatterns = [
    path('', home),
    path('create/', task_create_view, name='task-create'),
    path('<int:id>/update/', task_update_view, name='task-update'),
    path('<int:id>/delete/', task_delete_view, name='task-delete'),
    path('<int:id>', task_detail_view, name='task-detail')
]