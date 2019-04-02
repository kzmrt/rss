from django.urls import path, include
from . import views

app_name = 'feed'

urlpatterns = [
    # トップ画面
    path('', views.IndexView.as_view(), name='index'),
]