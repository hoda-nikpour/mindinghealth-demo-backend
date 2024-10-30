# accounts/urls.py
# accounts/urls.py
from django.urls import path
from .views import signup, login_view  # Import login_view here

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),  # Use login_view in the path
]
