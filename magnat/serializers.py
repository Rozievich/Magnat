from rest_framework.serializers import ModelSerializer
from rest_framework.fields import ReadOnlyField
from .models import Client, Media, Worker, Comment


class ClientModelSerializer(ModelSerializer):
    status = ReadOnlyField()
    sabab = ReadOnlyField()

    class Meta:
        model = Client
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = Client.objects.get(id=data['id'])
        data['status'] = user.get_status_display_text()
        return data


class MediaModelSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'


class WorkerModelSerializer(ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = Worker.objects.get(id=data['id'])
        data['sohasi'] = user.get_status_display_text()
        return data


class CommentModelSerializer(ModelSerializer):
    status = ReadOnlyField()

    class Meta:
        model = Comment
        fields = '__all__'
