from cryptography.fernet import Fernet
from django.db import models

from dotenv import load_dotenv
import os

load_dotenv('/home/ubuntu/.credentials/.env')

cipher = Fernet(os.getenv("ENCRYPTION_KEY").encode())

class Payment_Method(models.Model):
    id_x = models.AutoField(primary_key=True,unique=True)
    owner = models.CharField(max_length=255,unique=True)

    postal_code = models.IntegerField()
    address = models.CharField(max_length=255,unique=True)

    last4 = models.CharField(max_length=4)

    exp_month = models.IntegerField()
    exp_year = models.IntegerField()
    
    def dne_address(self, address, mode):
        if mode == 'e':
            self.address = cipher.encrypt(address.encode())
            return self.address
        else:
            return cipher.decrypt(self.address).decode()

    def dne_postal_code(self, postal_code, mode):
        if mode == 'e':
            self.postal_code = cipher.encrypt(postal_code.encode())
            return self.postal_code
        else:
            return cipher.decrypt(self.postal_code).decode()
    
    def dne_last4(self, last4, mode):
        if mode == 'e':
            self.last4 = cipher.encrypt(last4.encode())
            return self.last4
        else:
            return cipher.decrypt(self.last4).decode()
    
    def dne_exp_month(self, exp_month, mode):
        if mode == 'e':
            self.exp_month = cipher.encrypt(exp_month.encode())
            return self.exp_month
        else:
            return cipher.decrypt(self.exp_month).decode()
    
    def dne_exp_year(self, exp_year, mode):
        if mode == 'e':
            self.exp_year = cipher.encrypt(exp_year.encode())
            return self.exp_year
        else:
            return cipher.decrypt(self.exp_year).decode()

class Products_List(models.Model):
    id_x = models.AutoField(primary_key=True,unique=True)

    products = models.CharField(max_length=255,unique=True)
    owner = models.CharField(max_length=255,unique=True)

    sell_counter = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

class Income_List(models.Model):
    id_x = models.IntegerField(primary_key=True,unique=True)
    
    amount = models.CharField(max_length=255,unique=True)
    currency = models.CharField(max_length=255,unique=True)
    owner = models.CharField(max_length=255,unique=True)

    created_at = models.DateTimeField(auto_now_add=True)