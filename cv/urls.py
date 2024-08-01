from django.urls import path
from .views import CurriculumView

app_name = 'cv'

urlpatterns = [
    path('', CurriculumView.as_view(), name='home')

]

