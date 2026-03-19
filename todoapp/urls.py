from django.urls import path,include
from . import views
app_name="todoapp"
urlpatterns = [
    path("", views.index,name="index"),
    path("addTask/",views.addTask,name="addTask"),
    path("task/<int:task_id>/", views.taskDetail, name="taskDetail"),
    path("<int:task_id>/delete/",views.deleteTask,name="deleteTask"),
    path("update/<int:task_id>/",views.updateTask,name="updateTask")
]