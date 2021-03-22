from django.db import models
from users.models import Address, User, Person


class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)

    nickname = models.CharField(max_length=128, null=True, blank=True)
    property_type = models.CharField(max_length=128, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return '{} - {}'.format(self.user.username, self.nickname)

    class Meta:
        verbose_name = "1 - Property"
        verbose_name_plural = "1 - Properties"


class Contract(models.Model):
    property = models.ForeignKey(Property, on_delete=models.PROTECT)
    secondary_party = models.ForeignKey(Person, on_delete=models.PROTECT)

    starting_date = models.DateField(null=True, blank=True)
    ending_date = models.DateField(null=True, blank=True)

    auto_renew = models.BooleanField(default=False)

    rent_amount = models.IntegerField(null=False, blank=False)
    rent_due_date = models.DateField(null=True, blank=True)

    deposit_amount = models.IntegerField(null=False, blank=False)

    status = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return '{} - {}'.format(self.property.nickname, self.rent_amount)

    class Meta:
        verbose_name = "2 - Contract"
        verbose_name_plural = "2 - Contracts"


class Payment(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.PROTECT)

    amount = models.IntegerField(null=False, blank=False)
    due_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return '{} - {}'.format(self.contract, self.rent_amount)

    class Meta:
        verbose_name = "3 - Payment"
        verbose_name_plural = "3 - Payments"
