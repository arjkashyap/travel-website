from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('saunterer.urls')),
    url(r'^blog/', include('blog.urls')),
]

if settings.DEBUG:
    print("--------------- somethings happening ----" + str(settings.DEBUG))
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
