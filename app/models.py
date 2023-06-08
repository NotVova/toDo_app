from django.db import models


class ObjectiveValue(models.Model):
    value_name = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Важность'
        verbose_name_plural = 'Важность'

    def __str__(self):
        return self.value_name


class Objective(models.Model):
    name = models.CharField(max_length=128)
    objective = models.CharField(max_length=256)
    value = models.ForeignKey(to=ObjectiveValue, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.name
