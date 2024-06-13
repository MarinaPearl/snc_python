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


class ProductFace(models.Model):
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


class ProductBody(models.Model):
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


class UserHair(models.Model):
    email = models.CharField(max_length=250)
    description = models.CharField(max_length=10)
    dandruff = models.CharField(max_length=10)
    dyed = models.CharField(max_length=10)
    fallOut = models.CharField(max_length=10)

    def as_json(self):
        return dict(
            input_email=self.email,
            input_description=self.description,
            input_dandruff=self.dandruff,
            input_dyed=self.dyed,
            input_fallOut=self.fallOut,
        )


class UserBody(models.Model):
    email = models.CharField(max_length=250)
    description = models.CharField(max_length=10)
    dandruff = models.CharField(max_length=10)
    dyed = models.CharField(max_length=10)
    fallOut = models.CharField(max_length=10)

    def as_json(self):
        return dict(
            input_email=self.email,
            input_description=self.description,
            input_dandruff=self.dandruff,
            input_dyed=self.dyed,
            input_fallOut=self.fallOut,
        )


class UserFace(models.Model):
    email = models.CharField(max_length=250)
    description = models.CharField(max_length=10)
    dandruff = models.CharField(max_length=10)
    dyed = models.CharField(max_length=10)
    fallOut = models.CharField(max_length=10)

    def as_json(self):
        return dict(
            input_email=self.email,
            input_description=self.description,
            input_dandruff=self.dandruff,
            input_dyed=self.dyed,
            input_fallOut=self.fallOut,
        )
