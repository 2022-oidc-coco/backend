from django.db import models

# Create your models here.
class locationInfo(models.Model):
    # name = models.CharField(max_length=50)
    # title = models.CharField(max_length=50)
    # contents = models.TextField()
    # url = models.URLField()
    # email = models.EmailField()
    # cdate = models.DateTimeField(auto_now_add=True)
    video_id = models.CharField(max_length=50)
    place_name = models.CharField(max_length=50)
    publishTime = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    place_url = models.CharField(max_length=50)
    # address_6 = models.CharField(max_length=50)
    viewCount = models.IntegerField()
    # likeCount = models.IntegerField()
    x = models.DecimalField(max_digits = 24, decimal_places = 18)
    y = models.DecimalField(max_digits = 24, decimal_places = 18)

    # id varchar(32) not null,
    # place_name varchar(50) not null,
    # viewCount int,
    # publishTime varchar(50),
    # likeCount int,
    # x decimal(24,18),
    # y decimal(24,18),
    # category varchar(32),
    # place_url varchar(100),
    # address_6 varchar(32),
