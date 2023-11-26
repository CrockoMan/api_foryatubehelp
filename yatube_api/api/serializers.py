from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ['id', 'author', 'text', 'pub_date', 'image', 'group']
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        fields = ['id', 'author', 'text', 'created', 'post']
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'
        # fields = ['title', 'slug']


# class FollowSerializer(serializers.ModelSerializer):
#     user = serializers.SlugRelatedField(
#         read_only=True,
#         slug_field='username',
#         default=serializers.CurrentUserDefault(),
#     )
#     following = serializers.SlugRelatedField(slug_field='username',
#                                              queryset=User.objects.all())
#
#     class Meta:
#         model = Follow
#         fields = ['user', 'following']
class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(slug_field='username',
                                             queryset=User.objects.all())

    class Meta:
        fields = ('user', 'following', )
        model = Follow
        validators = [
            UniqueTogetherValidator(queryset=Follow.objects.all(),
                                    fields=('user', 'following'))
        ]

    def validate_following(self, value):
        request = self.context.get('request')
        user = request.user
        if user == value:
            raise serializers.ValidationError('Not applied following myself')
        return value