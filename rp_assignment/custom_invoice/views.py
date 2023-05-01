from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from xhtml2pdf import pisa
from .forms import Invoice_form

# Create your views here.

def generate_Invoice(request):
    # we check for request method "POST" which is generated on submission
    if request.method == 'POST':
        form = Invoice_form(request.POST)
        if form.is_valid():     
            # form becomes valid when the submit button is pressed and all of the required fields pass their validation checks 
            # Calculate total amount
            items = form.cleaned_data['items']
            total_amount=0
            for item in items.split('\n'):
                tempL = item.split(',')
                total_amount += float(tempL[1])*float(tempL[2])
            form.cleaned_data['total_amount'] = total_amount
            
            # creating a context dictionary that contains the cleaned form data
            context = {'form': form.cleaned_data}
            # creating an HTTP response object that will hold the generated PDF file
            response = HttpResponse(content_type='application/pdf')
            # giving filename to the file to be downloaded as attachment
            response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
            # loading the invoice template
            template = loader.get_template('invoice_template.html')
            # creating the source of the pdf, rendered template
            html = template.render(context)
            # generating pdf from html content
            pisa_status = pisa.CreatePDF(html, dest=response)
            if pisa_status.err:
                return HttpResponse('Error generating PDF file')
            # file downloads if reached here
            return response
    else:
        form = Invoice_form()
    return render(request, 'invoice_form.html', {'form': form})