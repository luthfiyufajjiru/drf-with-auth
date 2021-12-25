from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


# URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/documentation/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/account/', include('usersApp.api.urls'))
]