from django.db import models
from payments.models import Property


class InventoryItem(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    condition = models.CharField(max_length=128, null=True, blank=True)
    cost = models.IntegerField(null=True, blank=True)

    photo = models.ImageField(upload_to='Images/')

    def __str__(self):
        return '{} - {}'.format(self.name, self.cost)

    class Meta:
        verbose_name = "1 - InventoryItem"
        verbose_name_plural = "1 - InventoryItems"


class Inventory(models.Model):
    property = models.ForeignKey(Property, on_delete=models.PROTECT)
    inventory_items = models.ManyToManyField(InventoryItem)
    total_value = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.property.nickname, self.total_value)

    class Meta:
        verbose_name = "2 - Inventory"
        verbose_name_plural = "2 - Inventories"

