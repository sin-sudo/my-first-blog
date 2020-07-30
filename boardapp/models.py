from django.db import models

# Create your models here.
class BoardModel(models.Model):
  title = models.CharField(max_length = 100)
  content = models.TextField()
  author = models.CharField(max_length = 100)
  # 画像を保存する場所を指定、なにも指定しない場合はsetting.pyで設定
  images = models.ImageField(upload_to = '')
  good = models.IntegerField()
  read = models.IntegerField()
  # readtextは既読したユーザーのユーザー名を取得して二回以上既読をつけられないようにするための項目
  readtext = models.CharField(max_length = 100)
  def __str__(self):
    return self.title