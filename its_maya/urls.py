"""its_maya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import StaticViewSitemap, PostSitemap, ListsSitemap, NewsSitemap

admin.site.site_header=settings.ADMIN_SITE_HEADER
admin.site.site_title=settings.ADMIN_SITE_TITLE
admin.site.index_title=settings.ADMIN_INDEX_TITLE

sitemaps = {
    'static': StaticViewSitemap,
    'Post': PostSitemap,
    'Lists': ListsSitemap,
    'News': NewsSitemap
}

urlpatterns = [
    path('administrator/', admin.site.urls),
    path('', include('blog.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)