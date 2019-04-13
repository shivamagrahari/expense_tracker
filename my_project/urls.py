from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
import accounts
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/',accounts.views.home, name='home'),
    path('add/', accounts.views.add, name='add'),
    path('delete/', accounts.views.delete, name='delete'),
    path('update/', accounts.views.update, name='update'),
    path('updatedone/', accounts.views.updatedone, name='updatedone'),

]
