from django.db import models

class Album(models.Model):
    album_name = models.CharField(max_length=50, primary_key=True)
    place = models.CharField(max_length=50)
    date_pub = models.DateTimeField('date published')

    def __str__(self):
        return self.album_name


class Images(models.Model):
    album_name = models.ForeignKey(Album, db_column='album_name')
    image_name = models.CharField(max_length=40)
    image = models.FileField(null=True, blank=True)
    upload_dt = models.DateTimeField(auto_now=True, auto_now_add=False)
    like_cntr = models.IntegerField(default=0)
    description = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.image_name

    
class Comments(models.Model):
    image_name = models.ForeignKey(Images, db_column="image_name")
    comment = models.CharField(max_length=200)
    comment_dt = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.comment
    