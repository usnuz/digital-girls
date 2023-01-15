from django.urls import path
from .views import *


urlpatterns = [
    path('profile/', profile, name='profile-url'),
    path('edit-profile/', edit_profile, name='edit-profile-url'),
    path('edit-username/', edit_username, name='edit-username-url'),
    path('edit-profile-info/', edit_profile_info, name='edit-profile-info-url'),
    path('edit-password/', edit_password, name='edit-password-url'),
    path('delete-account/', delete_account, name='delete-account-url'),
    path('login/', log_in, name='login-url'),
    path('logout/', log_out, name='logout-url'),
    path('reset-password/', reset_password, name='reset-password-url'),
]
