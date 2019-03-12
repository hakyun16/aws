from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length = 255)
    image = models.ImageField(upload_to='images/') # 이미지를 데이터베이스에 넣고 싶을 때 bash 창에서 하나 설치해줘야함 => pip install pillow 파이썬으로 이미지를 효율적으로 처리하기 위한 것
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title