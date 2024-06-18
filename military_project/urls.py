from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('sub1/', views.sub1, name='sub1'),
    path('sub2/', views.sub2, name='sub2'),
    path('sub3/', views.sub3, name='sub3'),
    path('chat/<str:room_name>/', views.chat_room, name='chat_room'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
