from django.urls import path
from .views import urlView

app_name = "shortner"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('urls/', urlView.as_view()),
]