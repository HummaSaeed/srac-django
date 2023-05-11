from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_items, name='add-items'),
    path('all/', views.view_items, name='view_items'),
    path('update/<int:pk>/', views.update_items, name='update-items'),
     path('item/<int:pk>/delete/', views.delete_items, name='delete-items'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)