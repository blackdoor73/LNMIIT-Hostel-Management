from django.contrib.auth.models import User #importing django's inbuilt user Model
from django.db import models
from django.utils import timezone
#This models file is used to define the tables i.e. database schema
#here none of the primary keys have been defined by developers but django's automatic primary key generation has been used
#to specify a custom primary key in place of automatically generated one, specify primary_key=True on the required  field.
class Hostel(models.Model):
    hostel_number = models.CharField(max_length=2, null=False)
    warden = models.CharField(max_length=30, null=False)

    def __str__(self):
        val = "Hostel - " + str(self.hostel_number)
        return val


class Room(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, null=False) #Foreign key relationship
    room_num = models.IntegerField(null=False)
    wing = models.CharField(max_length=1, null=False)
    floor = models.IntegerField(null=False)
    capacity = models.IntegerField(null=False)
    status = models.IntegerField(null=False, default=0)

    def __str__(self):
        val = '-'.join([self.hostel.hostel_number, self.wing, str(self.floor*100 + self.room_num)])
        return val


class Student(models.Model):
    roll_num = models.ForeignKey(User, Room, null=False, db_column="username", unique=True)
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    mail = models.CharField(max_length=30, null=False)
    student_contact_num = models.BigIntegerField(null=False)
    guardian_contact_num = models.BigIntegerField(null=False)
    gender = models.CharField(max_length=1, null=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=False)

    def __str__(self):
        val = self.roll_num.username + '-' + self.first_name + '_' + self.last_name
        return val


class Feedback(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)


class Complaint(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    complaint = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)


class ChangeRoom(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    reason = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)

class Attendance(models.Model):
    txtReport = models.FileField(upload_to='static/AttendanceRecords', null=False)
    date = models.DateField(null=False)
