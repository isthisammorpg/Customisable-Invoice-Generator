from django import forms

class Invoice_form(forms.Form):
    # form elements
    seller_name = forms.CharField(label='Seller\'s Name', max_length=255)
    seller_email = forms.EmailField(label='Seller\'s Email', max_length=254)
    seller_address = forms.CharField(label='Seller\'s Address', widget=forms.Textarea)
    customer_name = forms.CharField(label='Customer\'s Name', max_length=255)
    customer_email = forms.EmailField(label='Customer\'s Email', max_length=254)
    customer_address = forms.CharField(label='Customer\'s Address', widget=forms.Textarea)
    invoice_number = forms.CharField(label='Invoice Number', max_length=20)
    invoice_date = forms.DateField(label='Invoice Date')
    due_date = forms.DateField(label='Due Date')
    items = forms.CharField(label='Items', widget=forms.Textarea)
    total_amount = forms.DecimalField(label='Total Amount', required=False)
