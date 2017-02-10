"""winter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from central import views as centralViews
from branch import views as branchViews

urlpatterns = [
    url(r'^$', centralViews.index),
    url(r'^about/', centralViews.about),
    url(r'^team/', centralViews.team),
    url(r'^branch/$', branchViews.index),

    # url(r'^column/(?P<column_link>[^/]+)/$', article_views.column_detail, name='column'),
    # url(r'^news/(?P<pk>\d+)/(?P<article_link>[^/]+)/$', article_views.article_detail, name='article'),

    url(r'^admin/', admin.site.urls),
]
