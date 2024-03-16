from django.db import models


# Create your models here.

class Product(models.Model):
    cost = models.IntegerField()
    name = models.CharField(max_length=20)

    def as_json(self):
        return dict(
            input_id=self.id,
            input_cost=self.cost,
            input_name=self.name,
        )