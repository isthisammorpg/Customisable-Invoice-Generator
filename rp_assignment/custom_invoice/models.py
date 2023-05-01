from django.db import models
# Create your models here.

class Invoice(models.Model):
    # model elements of invoice
    seller_name = models.CharField(max_length=255)
    seller_email = models.EmailField(max_length=254)
    seller_address = models.TextField()
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField(max_length=254)
    customer_address = models.TextField()
    invoice_number = models.CharField(max_length=20)
    invoice_date = models.DateField()
    due_date = models.DateField()
    items = models.TextField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
 