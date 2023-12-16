"""
URL configuration for djangoSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path('Math340/',include("Math340.urls")),
    path('WebsiteProgress/',include("WebsiteProgress.urls")),
    path('admin/', admin.site.urls),
    path('LeavingCert/',include("LeavingCert.urls")),
    path('Lin/',include("Lin.urls")),
    path('Misc/',include("Misc.urls")),
    path('Math_161/',include("Math_161.urls")),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)