from django.urls import path, include
from .views.SearchView import SearchView
from .views.PolicyView import PolicyView, GetAllPaginatedPolicy
from .views.AnalyticsView import AnalyticsView

urlpatterns = [
    path('search/',SearchView.as_view()),
    path('policy/<int:pk>',PolicyView.as_view()),
    path('allpolicy/',GetAllPaginatedPolicy.as_view()),
    path('chartdata/',AnalyticsView.as_view()),
]