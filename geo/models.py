from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Transport(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Paid(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Driver(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Auto(models.Model):
    gate = models.ForeignKey(Driver, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Geo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    perevozka = models.CharField(max_length=200, blank=True)
    act = models.CharField(max_length=200, blank=True)
    date_dilevery_sklad = models.DateField()
    date_departure = models.DateField(null=True, blank=True)
    date_planned_meet = models.DateField(null=True, blank=True)
    date_fact_meet = models.DateField(null=True, blank=True)
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city_from')
    from_transport = models.ForeignKey(Transport, on_delete=models.CASCADE, related_name='transport_from')
    through_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='th_city')
    through_transport = models.ForeignKey(Transport, on_delete=models.CASCADE, related_name='th_transport')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city_to')
    date_dilevery = models.DateField(null=True, blank=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    volume_sklad = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    places_sklad = models.PositiveIntegerField(null=True, blank=True)
    weight_sklad = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    places_sender = models.PositiveIntegerField()
    volume_sender = models.DecimalField(max_digits=10, decimal_places=2)
    weight_sender = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_receipt = models.CharField(max_length=255, blank=True)
    price_dilevery = models.DecimalField(max_digits=10, decimal_places=2)
    cost_dilevery = models.DecimalField(max_digits=10, decimal_places=2)
    paid_driver = models.ForeignKey(Paid, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-created']
