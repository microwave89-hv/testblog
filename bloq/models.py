from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class MyBlogPost(models.Model):
    myauthor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    mytitle = models.CharField(max_length = 200)
    mytext = models.TextField()
    yourcreateddate = models.DateTimeField(default = timezone.now())
    thepublishdate = models.DateTimeField(blank = True, null = True)

    def publishpost(self):
        thepublishdate = timezone.now()
        self.save()

    def __str__(self):
        return self.mytitle