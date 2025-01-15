from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Post(models.Model):
    image = models.ImageField(upload_to = 'posts/', null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    tag = models.ManyToManyField('Tag', related_name='posts', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name= ' post Esli ne ponimaesh uchi angl'
        verbose_name_plural = 'Posts'

