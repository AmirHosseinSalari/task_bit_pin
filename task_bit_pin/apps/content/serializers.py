from task_bit_pin.apps.content.models import Content, Score
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ContentSerializer(serializers.HyperlinkedModelSerializer):
    scor_count = serializers.IntegerField()
    star_avg = serializers.IntegerField()

    class Meta:
        model = Content
        fields = ['title', 'text', 'scor_count', 'star_avg']


class AddScoreSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        print(validated_data)
        score = Score.objects.get(
            user_id=validated_data.get('user_id', None),
            content_id=validated_data.get('content_id', None)
        )
        if score:
            score = Score.objects.update(
                user_id=validated_data.get('user_id', None),
                content_id=validated_data.get('content_id', None),
                stars=validated_data.get('stars', None)
            )
        else:
            score = Score.objects.create(
                user_id=validated_data.get('user_id', None),
                content_id=validated_data.get('content_id', None),
                stars=validated_data.get('stars', None)
            )
        return score

    class Meta:
        model = Score
        fields = ['content_id', 'user_id', 'stars']
