from django.db import models


# Create your models here.

class Product(models.Model):
    urlImage = models.CharField(max_length=500)
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    typeProblem = models.CharField(max_length=1500)

    def as_json(self):
        return dict(
            input_id=self.id,
            input_urlImage=self.urlImage,
            input_brand=self.brand,
            input_name=self.name,
            input_description=self.description,
            input_typeProblem=self.typeProblem,
        )
