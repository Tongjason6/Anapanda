"""commitments URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path

from django.contrib import admin
from django.contrib.auth import views as auth_views
#Putting login required here for now
from django.contrib.auth.decorators import login_required

from commitments.apps.accounts import views as accounts_views
from commitments.apps.managetime import views as kuviews

urlpatterns = [   
    path('accounts/signup/', accounts_views.signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('kummit/', login_required(kuviews.kummithome), name='kummithome'),
    path('kummit/<int:pk>/', login_required(kuviews.TaskUpdate.as_view()), name='kummit-view'),
    path('kummit/tasks/make/', login_required(kuviews.TaskCreate.as_view()), name='task-create'),
    path('kummit/tasks/<int:pk>/', login_required(kuviews.TaskView.as_view()), name='task-detail'),
    path('kummit/tasks/<int:pk>/delete/', login_required(kuviews.TaskDelete.as_view()), name='kummit-delete'),
    path('kummit/tasks/', login_required(kuviews.TaskList.as_view()), name='task-list'),
    path('kummit/kummitments/make/', login_required(kuviews.KummitmentCreate.as_view()), name='kummitment-make'),
    path('kummit/kummitments/<int:pk>/', login_required(kuviews.KummitmentView.as_view()), name='kummitment-detail'),
    path('kummit/kummitments/', login_required(kuviews.KummitmentList.as_view()), name='kummitment-list'), 
    path('kummit/circles/<int:pk>/', login_required(kuviews.CircleView.as_view()), name='circle-detail'),
    path('kummit/circles/', login_required(kuviews.CircleList.as_view()), name='circle-list'),
    path('kummit/roles/<int:pk>/', login_required(kuviews.RoleView.as_view()), name='role-detail'),
    path('kummit/roles/', login_required(kuviews.RoleList.as_view()), name='role-list'), 
    
    path('', login_required(kuviews.kummithome), name='home'),
]

urlpatterns += [
    path('admin/', admin.site.urls),
]