from django.db import models

# Create your models here.

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    student_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    year_level = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    birthday = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    birthday = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=50)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
    
class AccountPayable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    payable_id = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    due_date = models.CharField(max_length=50)
    amount = models.BigIntegerField()

    def __str__(self):
        return (f"{self.description} {self.amount}")

class Payment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Record, on_delete=models.CASCADE)
    payable = models.ForeignKey(AccountPayable, on_delete=models.CASCADE)
    amount_paid = models.BigIntegerField()
    receiver_user_id = models.CharField(max_length=20)
    payment_date = models.CharField(max_length=50)

    def __str__(self):
        return (f"{self.student} {self.amount_paid}")

class Expense(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=50)
    amount = models.BigIntegerField()
    date = models.CharField(max_length=50)

    def __str__(self):
        return (f"{self.description} {self.amount}")

class Treasurer(models.Model):
    user = models.OneToOneField(Record, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.user}")

class MoneyTransfer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    treasurer = models.ForeignKey(Treasurer, on_delete=models.CASCADE)
    admin_id = models.CharField(max_length=20)
    amount_transferred = models.BigIntegerField()
    date_transferred = models.CharField(max_length=50)

    def __str__(self):
        return (f"{self.treasurer} {self.amount_transferred}")