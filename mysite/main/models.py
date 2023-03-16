from django.db import models


#Основная таблица
class Car(models.Model):
    model_name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    brand = models.ForeignKey('CarBrand', on_delete=models.CASCADE)
    body = models.ForeignKey('Body', on_delete=models.CASCADE)
    drive = models.ForeignKey('Drive', on_delete=models.CASCADE)
    transmission = models.ForeignKey('Transmission', on_delete=models.CASCADE)
    color = models.ForeignKey('Color', on_delete=models.CASCADE)


# Базовые таблицы
class CarBrand(models.Model):
    brand_name = models.CharField(max_length=50)

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name_plural = 'Car Brands'


class Body(models.Model):
    body_name = models.CharField(max_length=55)

    def __str__(self):
        return self.body_name

    class Meta:
        verbose_name_plural = 'Bodies'


class Drive(models.Model):
    drive_name = models.CharField(max_length=55)

    def __str__(self):
        return self.drive_name

    class Meta:
        verbose_name_plural = 'Drives'


class Transmission(models.Model):
    transmission_name = models.CharField(max_length=60)

    def __str__(self):
        return self.transmission_name

    class Meta:
        verbose_name_plural = 'Transmissions'


class Color(models.Model):
    color_name = models.CharField(max_length=60)

    def __str__(self):
        return self.color_name

    class Meta:
        verbose_name_plural = 'Colors'


