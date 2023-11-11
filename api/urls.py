from django.urls import include, path
from rest_framework import routers
from api.views.profile_views import profiles_detail, profiles_list
from api.views.transaction_views import transactions_detail, transactions_list


urlpatterns = [
    path('profiles/', profiles_list),
    path('profiles/<int:pk>/', profiles_detail),
    path('transactions/', transactions_list),
    path('transactions/<int:pk>/', transactions_detail)
]
