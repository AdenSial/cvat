from django.db.models import Count
from rest_framework import viewsets
from rest_framework.response import Response

from cvat.apps.engine.models import LabeledShape, Task
from cvat.apps.engine.permissions import TaskPermission


class AnnotationStatsTaskPermission(TaskPermission):
    """
    Reuse CVAT's existing TaskPermission but require
    annotation-view access for our analytics endpoint.
    """

    @classmethod
    def _get_scopes(cls, request, view, obj):
        if view.action == "retrieve" and request.method == "GET":
            return [cls.Scopes.VIEW_ANNOTATIONS]

        return super()._get_scopes(request, view, obj)


class AnnotationStatsViewSet(viewsets.GenericViewSet):
    """
    Returns annotation counts grouped by label for one task.
    """

    queryset = Task.objects.all()
    search_fields = []
    ordering_fields = ["id"]
    ordering = ["id"]
    iam_permission_class = AnnotationStatsTaskPermission

    def retrieve(self, request, pk=None):
        task = self.get_object()

        counts = (
            LabeledShape.objects
            .filter(job__segment__task_id=task.id)
            .values("label_id", "label__name")
            .annotate(count=Count("id"))
            .order_by("-count", "label__name")
        )

        return Response(
            {
                "task_id": task.id,
                "total_annotations": sum(item["count"] for item in counts),
                "counts": [
                    {
                        "label_id": item["label_id"],
                        "label": item["label__name"],
                        "count": item["count"],
                    }
                    for item in counts
                ],
            }
        )