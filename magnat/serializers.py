from rest_framework.serializers import ModelSerializer
from rest_framework.fields import ReadOnlyField
from .models import Mijoz, Portfolio, Hodim, Comment, PortfolioKategoriya, Blog
from .utils import send_message


class ClientModelSerializer(ModelSerializer):
    status = ReadOnlyField()
    sabab = ReadOnlyField()
    sana = ReadOnlyField()

    class Meta:
        model = Mijoz
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = Mijoz.objects.get(id=data['id'])
        data['status'] = user.get_status_display_text()
        return data

    def create(self, validated_data):
        text = f"Ism: {validated_data.get('ism')}\nTelefon Raqam: {validated_data.get('tel_nomer')}"
        send_message(text)
        return super().create(validated_data)


class MediaModelSerializer(ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        category = PortfolioKategoriya.objects.get(id=data['category'])
        data['category'] = category.title
        return data


class WorkerModelSerializer(ModelSerializer):
    class Meta:
        model = Hodim
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = Hodim.objects.get(id=data['id'])
        data['sohasi'] = user.get_status_display_text()
        return data


class CommentModelSerializer(ModelSerializer):
    status = ReadOnlyField()

    class Meta:
        model = Comment
        fields = '__all__'


class BlogModelSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = 'id', 'title', 'summary', 'picture', 'created_at'
