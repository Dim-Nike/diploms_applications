from django.db import models


class UserProfile(models.Model):
    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'

    name = models.CharField(verbose_name='Имя', max_length=155)
    link = models.CharField(verbose_name='Соц. сеть', max_length=155)

    def __str__(self):
        return self.name

class DevFile(models.Model):
    class Meta:
        verbose_name = 'Наработанные файл'
        verbose_name_plural = 'Наработанные файлы'

    dsc = models.TextField(verbose_name='Описание')
    file = models.FileField(verbose_name='Файл', upload_to='dev_file/file/%Y/%m/%d/')

class ScientificSupervisor(models.Model):
    class Meta:
        verbose_name = 'Научный руководитель'
        verbose_name_plural = 'Научные руководители'

    name = models.CharField(verbose_name='ФИО', max_length=155)

    def __str__(self):
        return self.name

class PaymentUser(models.Model):
    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

    paid = models.IntegerField(verbose_name='Оплата')
    data_start = models.DateField(verbose_name='Дата создания', auto_now_add=True)

    def __str__(self):
        return str(self.paid)
class LastFile(models.Model):
    class Meta:
        verbose_name = 'Последняя редакция'
        verbose_name_plural = 'Последние редакции'

    data_start = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    file = models.FileField(verbose_name='Файл', upload_to='dev_file/file/%Y/%m/%d/')
    comment_self = models.TextField(verbose_name='Комментарий', null=True, blank=True)
    comment_user = models.TextField(verbose_name='Комментарий заказчика', null=True, blank=True)


class Application(models.Model):
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявка'

    user_name = models.ForeignKey(UserProfile, verbose_name='Заказчик', on_delete=models.PROTECT)
    topic = models.CharField('Тема диплома', max_length=155)
    scientific_supervisor = models.ForeignKey(ScientificSupervisor, verbose_name='Научный руководитель', on_delete=models.PROTECT)
    developments = models.ManyToManyField(DevFile, verbose_name='Наработанные данные', null=True, blank=True)
    last_file = models.ManyToManyField(LastFile, verbose_name='Последняя редакция', null=True, blank=True)
    price = models.IntegerField(verbose_name='Цена диплома')
    paid = models.ManyToManyField(PaymentUser, verbose_name='Оплата', null=True, blank=True)
    is_technical_part = models.BooleanField(verbose_name='Разработан сайт')
    is_design = models.BooleanField(verbose_name='Разработан дизайн')
    link_site = models.CharField(verbose_name='Ссылка на сайт', max_length=255)
    link_figma = models.CharField(verbose_name='Ссылка на фигму', max_length=255)

