"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from mytodoapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name ='home'),
    path('add/',views.add,name = 'add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('edit/<int:taskid>/',views.edit,name='edit'),
    path('cbvindex/',views.TaskListView.as_view(),name="cbv_index"),
    path('cbvdetail/<int:pk>/',views.TaskDetailView.as_view(),name = "detailview"),
    path('cbvupdate/<int:pk>/',views.TaskupdateView.as_view(),name="cbvupdate"),
    path('cbvdelete/<int:pk>/',views.Taskdeleteview.as_view(),name="deletecbv")
]
