from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
MAX_LENGTH = 30


class Group(models.Model):
    title = models.CharField('Наименование', max_length=200)
    slug = models.SlugField('slug', max_length=50, unique=True)
    description = models.CharField('Описание', max_length=200)

    def __str__(self):
        return self.title[:MAX_LENGTH]


class Follow(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='follow')
    following = models.ForeignKey(User,
                                  on_delete=models.CASCADE,
                                  related_name='following')


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='posts')
    image = models.ImageField(upload_to='posts/',
                              null=True,
                              blank=True)
    group = models.ForeignKey(Group,
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True,)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        default_related_name = 'posts'
        ordering = ('pub_date', )

    def __str__(self):
        return self.text[:MAX_LENGTH]


class Comment(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comments')
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    text = models.TextField('Комментарий',)
    created = models.DateTimeField('Дата добавления',
                                   auto_now_add=True,
                                   db_index=True)

    def __str__(self):
        return self.text[:MAX_LENGTH]
