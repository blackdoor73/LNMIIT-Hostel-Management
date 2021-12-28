from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'management'

urlpatterns = [
    path('', views.signin, name='signin'),
    path('room_change_request/', views.roomChangeRequest, name='roomChangeRequest'),
    path('menu/', views.menu, name='menu'),
    path('feedback/', views.feedback, name='feedback'),
    path('complaint/', views.complaint, name='complaint'),
    path('profile/', views.profile, name='profile'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
