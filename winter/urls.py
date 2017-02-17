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
from django.conf.urls import include, url
from django.contrib import admin
from central import views as centralViews
from branch import views as branchViews
from django.contrib.auth.views import login, logout
from DjangoUeditor import urls as DjangoUeditor_urls

urlpatterns = [
    url(r'^$', centralViews.index),
    url(r'^about/', centralViews.about),
    url(r'^commi/send', centralViews.sendEmail),
    url(r'^commi/join', centralViews.joinUs),
    url(r'^login$', centralViews.login),
    url(r'^login/commit$', centralViews.loginCommit),
    url(r'^logout$', centralViews.logout),
    url(r'^signup$', centralViews.signup),
    url(r'^signup/commit$', centralViews.signupCommit),
    url(r'^branch/$', branchViews.index),
    url(r'^branch/tools$', branchViews.tools),
    url(r'^branch/column/(\d+)$', branchViews.column),
    url(r'^branch/column/(\d+)/(\d+)$', branchViews.columnPage),
    url(r'^branch/article/(\d+)$', branchViews.article),
    url(r'^branch/bbs$', branchViews.bbs),
    url(r'^branch/bbs/(\d+)$', branchViews.bbsPage),
    url(r'^branch/bbs/post$', branchViews.bbsPost),
    url(r'^branch/bbs/post/(\d+)$', branchViews.post),
    url(r'^branch/bbs/post/reply/(\d+)$', branchViews.postReply),

    url(r'^ueditor/', include(DjangoUeditor_urls)),
    url(r'^admin/', admin.site.urls),
]
