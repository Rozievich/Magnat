from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet
from .serializers import ClientModelSerializer, MediaModelSerializer, WorkerModelSerializer, CommentModelSerializer
from .models import Mijoz, Portfolio, Hodim, Comment

class ClientModeViewSet(ModelViewSet):
    queryset = Mijoz.objects.all()
    serializer_class = ClientModelSerializer
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser]
    http_method_names = ("post", )


class MediaModelViewSet(ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = MediaModelSerializer
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser]
    http_method_names = ("get", )


class WorkerModelViewSet(ModelViewSet):
    queryset = Hodim.objects.all()
    serializer_class = WorkerModelSerializer
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser]
    http_method_names = ("get", )


class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.filter(status=True)
    serializer_class = CommentModelSerializer
    permission_classes = [AllowAny]
    http_method_names = ("post", "get")