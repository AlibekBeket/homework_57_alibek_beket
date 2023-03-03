from django.db import models


class Issue(models.Model):
    summary = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Краткое описание"
    )
    description = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="Полное описание"
    )
    status = models.ForeignKey(
        'issue_tracker.Status',
        on_delete=models.CASCADE,
        related_name='status',
        verbose_name='Статус'
    )
    type = models.ForeignKey(
        'issue_tracker.Type',
        on_delete=models.CASCADE,
        related_name='type',
        verbose_name='Тип'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Время обновления'
    )

    def __str__(self):
        return f"{self.summary} - {self.status}"
