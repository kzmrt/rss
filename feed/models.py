from django.db import models

class Rss(models.Model):
    """RSSモデル"""
    class Meta:
        db_table = 'rss'

    title = models.CharField(verbose_name='タイトル', max_length=255)
    link = models.CharField(verbose_name='リンク', max_length=255, default='')
    category = models.CharField(verbose_name='カテゴリ', max_length=255, default='', blank=True)
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    def __str__(self):
        return self.title + ',' + self.text
