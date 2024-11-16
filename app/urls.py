from django.urls import path
from .views import TravelView, KlassView, MehmonxonaView

urlpatterns = [
    path('travels/', TravelView.as_view(), name='travel-list'),
    path('travels/<int:pk>/', TravelView.as_view(), name='travel-detail'),
    path('klasses/', KlassView.as_view(), name='klass-list'),
    path('klasses/<int:pk>/', KlassView.as_view(), name='klass-detail'),
    path('mehmonxonalar/', MehmonxonaView.as_view(), name='mehmonxona-list'),
    path('mehmonxonalar/<int:pk>/', MehmonxonaView.as_view(), name='mehmonxona-detail'),
]
