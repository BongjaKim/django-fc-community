from django.db import models

# Create your models here.


class Fcuser(models.Model):
    username = models.CharField(max_length=64, verbose_name='User Name')
    password = models.CharField(max_length=64, verbose_name='Password')
    useremail = models.EmailField(max_length=64, verbose_name='E-mail')
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='Resistered Time')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'fc_community'
        verbose_name_plural = "패스트캠퍼스 사용자"
        verbose_name = "패스트캠퍼스 사용자"
