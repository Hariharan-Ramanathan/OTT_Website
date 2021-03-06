"""OTT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from thumbnails.views import home, home_dyn, thumbnail_list, create_form, register_form, login_form, logOut, filter_data, edit_delete, upload, front_page
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',front_page, name="ott"),
    path("OTT/create-form/<int:req_id>",create_form, name='req_id'),
    path('all/',thumbnail_list),
    path('movie/<str:req_id>',home_dyn),
    path('register',register_form, name="register"),
    path('login',login_form, name="login"),
    path('logout',logOut, name = 'logout'),
    path('filter',filter_data, name = 'filter'),
    path('OTT/delete/<int:req_id>/',edit_delete , name = 'req_id'),
    path('upload/',upload, name="upload"),
    path('OTT/',home, name='home')
    ] 
 
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
