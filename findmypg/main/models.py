from django.db import models

class owner(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    phone=models.IntegerField()
    email=models.EmailField(max_length=30)
    photo=models.FileField()

class user(models.Model):
    name=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    age=models.IntegerField()
    address=models.CharField(max_length=30)
    phone=models.IntegerField()
    email=models.EmailField(max_length=30)
    photo=models.FileField()

class pg(models.Model):
    ownerid=models.ForeignKey(owner, on_delete=models.CASCADE)
    address=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    pin=models.IntegerField()
    rent=models.DecimalField(max_digits=10,decimal_places=2)
    occupancy=models.IntegerField()
    forgender=models.CharField(max_length=30)
    size=models.IntegerField()
    rooms=models.IntegerField()
    intime=models.DateTimeField()
    outtime=models.DateTimeField()

class ameneties(models.Model):
    pgid=models.ForeignKey(pg,on_delete=models.CASCADE)
    ac=models.BooleanField()
    watercooler=models.BooleanField()
    waterpurifier=models.BooleanField()
    geyser=models.BooleanField()
    bed=models.BooleanField()
    wifi=models.BooleanField()
    meals=models.BooleanField()
    parking=models.BooleanField()

class favourites(models.Model):
    userid=models.ForeignKey(user,on_delete=models.CASCADE)
    pgid=models.ForeignKey(pg,on_delete=models.CASCADE)

class ratings(models.Model):
    userid=models.ForeignKey(user,on_delete=models.CASCADE)
    pgid=models.ForeignKey(pg,on_delete=models.CASCADE)
    rating=models.IntegerField()
    review=models.CharField(max_length=30)
    date=models.DateField()

class contactowner(models.Model):
    userid=models.ForeignKey(user,on_delete=models.CASCADE)
    pgid=models.ForeignKey(pg,on_delete=models.CASCADE)
    message=models.CharField(max_length=30)
    datetime=models.DateTimeField()

class pgimages(models.Model):
	pgid=models.ForeignKey(pg,on_delete=models.CASCADE)
	image=models.FileField()
