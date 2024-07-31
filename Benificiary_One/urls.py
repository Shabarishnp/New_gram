"""Benificiary_One URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from FirstApp.views import *

urlpatterns = [
    path('',Home, name='home'),
    path('loginpage',LoginPage, name='loginpage'),
    path('logindetails',LoginDetails, name='logindetails'),
    path('addcategory',AddCategory, name='addcategory'),
    path('addscheme',AddScheme, name='addscheme'),
    path('filterbene',FilterBene, name='filterbene'),
    path('add_category',Add_Category, name='add_category'),
    path('view_category',View_Category, name='view_category'),
    path('add_scheme',Add_Scheme, name='add_scheme'),
    path('register',Register, name='register'),
    path('view_scheme',View_Scheme, name='view_scheme'),
    path('state_uts', State_Uts, name='state_uts'),
    path('registeruser', RegisterUser, name='registeruser'),
    path('home_categories', Home_Categories, name='home_categories'),
    path('home_ministeries', Home_Ministeries, name='home_ministeries'),
    path('home_eligibility', Home_Eligibility, name='home_eligibility'),
    path('edit_scheme/<str:pid>', Edit_Scheme, name='edit_scheme'),
    path('delete_scheme/<str:pid>', Delete_Scheme, name='delete_scheme'),
    path('view_scheme_state/<str:pid>', View_Scheme_State, name='view_scheme_state'),
    path('view_beneficiary/<str:pid>', View_Beneficiary, name='view_beneficiary'), 
    path('add_eligibility/<str:pid>',Add_Eligibility, name='add_eligibility'),
    path('mail_all/<str:pid>',Mail_All, name='mail_all'),
    path('add_eligibility_value',Add_Eligibility_Value, name='add_eligibility_value'),
    path('user_page', User_Page, name='user_page'),
    path('user_scheme/<str:pid>', User_Scheme, name='user_scheme'),
    path('apply_scheme/<str:pid>', Apply_Scheme, name='apply_scheme'),
    path('delete_category/<str:pid>', Delete_Category, name='delete_category'),
    path('edit_category/<str:pid>', Edit_Category, name='edit_category'),
    path('update_category', Update_Category, name='update_category'),
    path('update_scheme', Update_Scheme, name='update_scheme'),
    path('about',About,name='about'),
    path('admin/', admin.site.urls),
]
