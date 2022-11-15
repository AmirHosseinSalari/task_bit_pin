from task_bit_pin.apps.content.models import Content, Score
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from django.db.models import Q, Sum, Count, Avg
from task_bit_pin.apps.content.serializers import UserSerializer, GroupSerializer, ContentSerializer, AddScoreSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContentListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ContentList to be viewed .
    """
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def get_queryset(self):
        return Content.objects.annotate(
            scor_count=Count('scores'),
            star_avg=Avg('scores')
        )

    permission_classes = [permissions.IsAuthenticated]


class AddScoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Scores to be viewed or edited. .
    """
    queryset = Score.objects.all()
    serializer_class = AddScoreSerializer
    filter_fields = ("content_id", "user_id")
    permission_classes = [permissions.IsAuthenticated]
