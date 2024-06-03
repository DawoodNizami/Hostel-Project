from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ad/<int:ad_id>/', views.detail, name='detail'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('post_ad/', views.post_ad, name='post_ad'),
    path('my_ads/', views.my_ads, name='my_ads'),
    path('my_ads/edit/<int:ad_id>/', views.edit_ad, name='edit_ad'),
    path('my_ads/delete/<int:ad_id>/', views.delete_ad, name='delete_ad'),
    path('profile/', views.profile, name='profile'),
]

