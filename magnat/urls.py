from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientModeViewSet, MediaModelViewSet, WorkerModelViewSet, CommentModelViewSet

router = DefaultRouter()
router.register("client", ClientModeViewSet, basename="client")
router.register('media', MediaModelViewSet, basename="media")
router.register('staff', WorkerModelViewSet, basename="staff")
router.register('comment', CommentModelViewSet, basename="comment")

urlpatterns = [
    path('', include(router.urls))
]
