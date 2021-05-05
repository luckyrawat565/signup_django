from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.index, name= 'home'),
    path('login/',views.user_login, name= 'login'),
    path('profile/', views.user_profile, name ='profile'),
    path('logout/',views.user_logout, name = 'logout'),
    path('signup/',views.user_signup, name = "signup"),
    path('dashboard/',views.user_dashboard, name ="dashboard"),
    path('addpost/', views.add_post, name = 'addpost'),
    path('updatepost/<int:id>',views.update_post , name ='updatepost'),
    path('delete/<int:id>', views.delete_post, name="deletepost"),
    

]
