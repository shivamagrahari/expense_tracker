from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
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
    path('sortbyname/', accounts.views.sortbyname, name='sortbyname'),
    path('sortbyname_/', accounts.views.sortbyname_, name='sortbyname_'),
    path('sortbycost/', accounts.views.sortbycost, name='sortbycost'),
    path('sortbycost_/', accounts.views.sortbycost_, name='sortbycost_'),
    path('sortbydate/', accounts.views.sortbydate, name='sortbydate'),
    path('sortbydate_/', accounts.views.sortbydate_, name='sortbydate_'),
    path('sortbyimage/', accounts.views.sortbyimage, name='sortbyimage'),
    path('sortbyimage_/', accounts.views.sortbyimage_, name='sortbyimage_'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)