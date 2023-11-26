from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupsViewSet, PostViewSet

app_name = 'api'

v1_router = DefaultRouter()

v1_router.register('groups', GroupsViewSet, basename='groups')
v1_router.register('follow', FollowViewSet, basename='follows')
v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet,
                   basename='comments')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    # path('v1/jwt/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('v1/', include('djoser.urls.jwt')),
]
