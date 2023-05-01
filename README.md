# Customizable Invoice Generator

This is a customizable invoice generator web application built using Django, Python, HTML, and CSS. The application allows users to generate and download customized invoices in PDF format.

## Installation

1. Clone the repository.
2. Activate the virtual environment using `source projectEnv/bin/activate`.
3. Intall these packages(if not installed): python3, pip3, django, xhtml2pdf
4. Run the application from the rp_assignment folder just one level after the root folder: `python3 manage.py runserver`

## Usage

1. Start the server.
2. Open your web browser and go to http://localhost:8000/generate-invoice or http://127.0.0.1:8000/generate-invoice
3. Fill out the form with your invoice details, invoice number, and customer details.
4. Click the ``Generate Invoice`` button to generate a PDF invoice.
5. Save and print the generated invoice as needed.

## Customization

This project is highly customizable and can be adapted to meet your specific needs. If you want to customize the appearance or content of the invoice, you can modify the `invoice_template.html` file in the `templates` directory. This file uses HTML and CSS to define the layout and style of the invoice. Some possible customizations include:

* Adding new fields to the invoice form.
* Changing the styling of the generated PDF.
* Adding support for multiple invoice templates.
* Adding support for multiple languages.

A sample invoice has been added in the Sample_Invoice folder showing the current level of customization.

[Note]:You may need to modify some other files as well depending upon your depth of customization.