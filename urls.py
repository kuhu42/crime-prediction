from django.contrib import admin
from django.urls import path, include
from .views import user_login, home
urlpatterns = [
path('admin/', admin.site.urls),
path('', include('loginanalysis.urls')),
path('login/', user_login, name='login'),
path('home/', home, name='home'),
]
