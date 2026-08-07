from django.urls import path
from tasks.views import dashboard, user_dashboard

urlpatterns = [
    path("dashboard/", dashboard ),
    path("user_dashboard/", user_dashboard ),
]