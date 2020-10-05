from django.db import models


HEADER_POSITION = (
    ('F', 'Firts'),
    ('S', 'Second'),
    ('T', 'Third'),
)


class Header(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    img = models.ImageField(upload_to='headers/')
    position = models.CharField(max_length=1, choices=HEADER_POSITION, unique=True, blank=True, null=True)
    caption_title = models.CharField(max_length=35, blank=True, null=True)
    caption_content = models.CharField(max_length=65, blank=True, null=True)
    caption_button = models.URLField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
