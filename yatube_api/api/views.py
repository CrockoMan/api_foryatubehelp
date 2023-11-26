from posts.models import Group, Post
from rest_framework import filters, permissions, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination

from api.permissions import OwnerOrReadOnly
from api.serializers import (CommentSerializer, FollowSerializer,
                             GroupSerializer, PostSerializer)


class GroupsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username', )

    def get_queryset(self):
        """Получение подписок пользователя."""
        current_user = self.request.user
        return current_user.follow.all()

    def perform_create(self, serializer):
        """Создание подписки."""
        return serializer.save(user=self.request.user)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    pagination_class = LimitOffsetPagination
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          OwnerOrReadOnly)

    def perform_create(self, serializer):
        """Создание поста."""
        return serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        """Создание поста."""
        return serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (OwnerOrReadOnly,)

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        """Выбрать все подписки пользователя."""
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        """Создание поста."""
        return serializer.save(author=self.request.user,
                               post=self.get_post())

    def perform_update(self, serializer):
        """Создание поста."""
        return serializer.save(author=self.request.user)
