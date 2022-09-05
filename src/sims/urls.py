from django.urls import path
from . import views


urlpatterns = [
    path('sims/', views.sim_list),
    path('sims/<int:pk>/', views.sim_detail)
]