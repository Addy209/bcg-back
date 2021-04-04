from django.urls import path, include
from .views.SearchView import SearchView
from .views.PolicyView import GetPolicyView, GetAllPaginatedPolicy
from .views.AnalyticsView import AnalyticsView

urlpatterns = [
    path('search/',SearchView.as_view()),
    path('getpolicy/<int:pk>',GetPolicyView.as_view()),
    path('getallpolicy/',GetAllPaginatedPolicy.as_view()),
    path('getchartdata/',AnalyticsView.as_view()),
]