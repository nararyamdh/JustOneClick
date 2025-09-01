from cryptography.fernet import Fernet
from django.db import models
import bcrypt

from dotenv import load_dotenv
import os

load_dotenv('/home/ubuntu/.credentials/.env')

cipher = Fernet(os.getenv("ENCRYPTION_KEY").encode())

class Users(models.Model):
    id_x = models.AutoField(primary_key=True,unique=True)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    email = models.CharField(max_length=255,unique=True)
    email_secondary = models.CharField(max_length=255,default="-")

    phone_number = models.CharField(max_length=255,default="-")

    birth_date = models.CharField(max_length=255,default="-")
    date_added = models.DateTimeField(auto_now_add=True)

    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)


class Authentication(models.Model):
    id_x = models.AutoField(primary_key=True,unique=True)

    email = models.CharField(max_length=255,unique=True)
    email_secondary = models.CharField(max_length=255,default="-")

    password = models.CharField(max_length=255)

    def set_password(self, raw_password):
        salt = bcrypt.gensalt(rounds=14)
        hashed = bcrypt.hashpw(raw_password.encode('utf-8'), salt)
        self.password = hashed.decode('utf-8')

    def check_password(self, raw_password):
        return bcrypt.checkpw(raw_password.encode('utf-8'), self.password.encode('utf-8'))

class Credit_Card(models.Model):
    id_x = models.AutoField(primary_key=True,unique=True)
    owner = models.CharField(max_length=255,unique=True)

    name = models.CharField(max_length=255,unique=True)
    address = models.CharField(max_length=255,unique=True)
    postal_code = models.IntegerField()

    last4 = models.CharField(max_length=4)

    exp_month = models.IntegerField()
    exp_year = models.IntegerField()

    token = models.CharField(max_length=200, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def dne_name(self, name, mode):
        if mode == 'e':
            self.name = cipher.encrypt(name.encode())
            return self.name
        else:
            return cipher.decrypt(self.name).decode()
    
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

    def dne_token(self, token, mode):
        if mode == 'e':
            self.token = cipher.encrypt(token.encode())
            return self.token
        else:
            return cipher.decrypt(self.token).decode()