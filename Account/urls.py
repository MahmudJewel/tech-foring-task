from django.urls import path
from Account import views

urlpatterns = [
    # path('login/', views.loginView, name='login'),
    # path('signup/', views.signupView, name='signup'),
    path('logout/', views.logoutView, name='logout'),
    path('profile/', views.profileView, name='user_profile'),
    path('change_password/', views.passwordChangeView, name='change_password'),
    path('profile_edit/', views.profileEdit, name='user_profile_edit'),
]
