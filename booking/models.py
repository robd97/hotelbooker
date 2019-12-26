# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Employees(models.Model):
    firstname = models.CharField(db_column='firstName', max_length=45)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=45)  # Field name made lowercase.
    ssn = models.CharField(db_column='SSN', max_length=11)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employees'

class Hotels(models.Model):
    hotelid = models.IntegerField(db_column='HotelID', primary_key=True)  # Field name made lowercase.
    stars = models.IntegerField(blank=True, null=True)
    numofrooms = models.IntegerField(db_column='NumOfRooms', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=45, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'hotels'


class Reservations(models.Model):
    reservationid = models.AutoField(db_column='reservationID', primary_key=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='startDate')  # Field name made lowercase.
    enddate = models.DateField(db_column='endDate')  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=45)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=45)  # Field name made lowercase.
    creditcardnum = models.CharField(db_column='creditCardNum', max_length=45)  # Field name made lowercase.
    phonenum = models.CharField(db_column='phoneNum', max_length=45)  # Field name made lowercase.
    hotel_hotelid = models.ForeignKey(Hotels, models.DO_NOTHING, db_column='hotel_HotelID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reservations'
        unique_together = (('reservationid', 'hotel_hotelid'),)

class Guests(models.Model):
    reservationid = models.ForeignKey('Reservations', models.DO_NOTHING, db_column='reservationID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=45)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'guests'


class Rooms(models.Model):
    number = models.IntegerField()
    day = models.DateField(primary_key=True)
    employees_ssn = models.ForeignKey(Employees, models.DO_NOTHING, db_column='employees_SSN')  # Field name made lowercase.
    reservation = models.ForeignKey(Reservations, models.DO_NOTHING, db_column='reservation', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rooms'
        unique_together = (('number', 'day'),)
