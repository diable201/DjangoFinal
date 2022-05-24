from django.db import models


class TimestampMixin(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Время последнего изменения'
    )


class BookJournalBase(TimestampMixin):
    class Meta:
        abstract = True
        verbose_name = 'Базовый класс литературы'
        verbose_name_plural = 'Базовые классы литературы'

    name = models.CharField(
        max_length=128,
        verbose_name='Название'
    )
    price = models.FloatField(
        default=0.0,
        verbose_name='Цена'
    )
    description = models.TextField(
        max_length=512,
        verbose_name='Описание'
    )

    def __str__(self):
        return f'{self.id}: {self.name} | {self.price}'


class Genre(TimestampMixin):
    name = models.CharField(
        max_length=200,
        verbose_name='Название'
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return f'{self.id}: {self.name}'


class Book(BookJournalBase):
    num_pages = models.IntegerField(
        default=0,
        verbose_name='Количество страниц'
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        null=True,
        related_name='book',
        verbose_name='Жанр'
    )

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Journal(BookJournalBase):
    BULLET = 'BULLET'
    FOOD = 'FOOD'
    TRAVEL = 'TRAVEL'
    SPORT = 'SPORT'

    JOURNAL_TYPE_CHOICES = (
        (BULLET, 'Bullet'),
        (FOOD, 'Еда'),
        (TRAVEL, 'Путешествия'),
        (SPORT, 'Спорт')
    )
    journal_type = models.CharField(
        choices=JOURNAL_TYPE_CHOICES,
        blank=True,
        max_length=255,
        verbose_name='Тип журнала'
    )
    publisher = models.TextField(
        blank=True,
        verbose_name='Автор'
    )

    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'
