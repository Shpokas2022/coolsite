from django.db import models

class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    # foto bus talpinamos i kataloga pagal datos sablona
    photo = models.ImageField(upload_to="photo/%Y/%m/%d")
    time_create = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title

