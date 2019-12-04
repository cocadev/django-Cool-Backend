from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('conduit.apps.articles.urls')),
    path('api/', include('conduit.apps.authentication.urls')),
    path('api/', include('conduit.apps.profiles.urls')),
    path('api/', include('conduit.apps.eugene.urls')),

]
