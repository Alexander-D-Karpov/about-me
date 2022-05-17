from django.urls import path

from .views import project

urlpatterns = [
    path("<int:id>", project, name="project")
]
