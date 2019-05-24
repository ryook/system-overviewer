from django.db import models

# Create your models here.

class System(models.Model):
    CATEGORY = [
        ("system", "system"),
        ("data_store", "dateStore")
    ]

    SERVICE = [
        ('internal', "internal"),
        ("outernal", "outernal")
    ]

    name = models.CharField(max_length=255)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY,
        default="system"
    )
    service = models.CharField(
        max_length=10,
        choices=SERVICE,
        default="internal"
    )
    memo = models.TextField(null=True, blank=True)
    layer = models.IntegerField(default=1)
    connect_to = models.ManyToManyField("self", verbose_name="接続先", blank=True)
    connect_from = models.ManyToManyField("self", verbose_name="接続元", blank=True)
    parent = models.ManyToManyField("self", verbose_name="親システム", blank=True)

    def __str__(self):
        return "{}(L{})".format(self.name, self.layer)