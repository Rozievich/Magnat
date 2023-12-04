from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientModeViewSet, MediaModelViewSet, WorkerModelViewSet, CommentModelViewSet, BlogModelViewSet

router = DefaultRouter()
router.register("client", ClientModeViewSet, basename="client")
router.register('media', MediaModelViewSet, basename="media")
router.register('staff', WorkerModelViewSet, basename="staff")
router.register('comment', CommentModelViewSet, basename="comment")
router.register('blog', BlogModelViewSet, basename="blog")

urlpatterns = [
    path('', include(router.urls))
]
