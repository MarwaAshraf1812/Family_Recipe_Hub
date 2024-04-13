from django.urls import path
from .views import signup, user_login, home, user_logout

app_name = 'accounts'

urlpatterns = [
    path('home/', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
