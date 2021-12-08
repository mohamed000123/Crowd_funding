from django.urls import path
from . import views
from accounts.views import signup
from django.contrib.auth import views as auth_views
app_name="accounts"
urlpatterns = [
    path('', signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(),name="logout"),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'),name="login"),
    path('profile/', views.profile , name="profile" ), 
    path('edit/', views.edit , name="edit" ),
    path('delete/', views.delete , name="delete" ),
    path('add/', views.add , name="add" ),
]
