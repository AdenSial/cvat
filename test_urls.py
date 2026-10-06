from django.urls import path
from .views import AnnotationStatsViewSet

urlpatterns = [
    path(
        "api/test/tasks/<int:pk>/annotation-stats/",
        AnnotationStatsViewSet.as_view({"get": "retrieve"}),
        name="annotation-stats",
    ),
]
