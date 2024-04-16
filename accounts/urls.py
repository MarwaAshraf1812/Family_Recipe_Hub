from django.urls import path
from .views import signup, user_login, user_logout

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
