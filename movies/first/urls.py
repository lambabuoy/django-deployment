from django.contrib import admin
from django.urls import path
from basic_app import views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view()),
    path('basic_app/', include('basic_app.urls',namespace='basic_app'))
]
