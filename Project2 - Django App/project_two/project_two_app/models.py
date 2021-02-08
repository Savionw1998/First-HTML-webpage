from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class AdminManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(postData["first_name"]) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData["last_name"]) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Email not valid"
        if len(postData['password']) < 3:
            errors["password"] = "password should be at least 3 characters"
        if postData['confirm_password'] != postData['password']:
            errors["confirm_password"] = "Passwords should match"
        return errors
    def product_validator(self, postData):
        errors = {}
        if len(postData["name"]) < 2:
            errors["name"] = "Name should be at least 2 characters"
        if len(postData["description"]) < 2:
            errors["description"] = "Description should be at least 2 characters"
        if len(postData["category"]) < 2:
            errors["category"] = "Category should be at least 2 characters"
        return errors

class AdminRegistration(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    confirm_password= models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AdminManager()

class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AdminManager()
