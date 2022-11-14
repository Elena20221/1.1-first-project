from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=100)
    price =models.DecimalField(max_digits=10, decimal_places=2)
    image = models.TextField()
    release_date =models.DateTimeField(auto_now_add=True)
    lte_exists =models.BooleanField()
    slug = models.SlugField()


    def __str__(self):
        return f"{self.id}: {self.name}"






