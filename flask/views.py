from datetime import datetime

from flask import jsonify, request

from models import invoices_schema, invoice_schema, Invoice
from app import app, db


@app.route('/api/invoices')
def get():
    invoice = Invoice.query.all()
    return invoices_schema.jsonify(invoice)


@app.route('/api/invoices/<invoice_id>')
def retrieve(invoice_id):
    invoice = Invoice.query.filter_by(InvoiceId=invoice_id)
    return jsonify(invoices_schema.dump(invoice))


@app.route('/api/invoices/add', methods=['POST'])
def add_invoice():
    new_invoice = Invoice(
        request.json['CustomerId'],
        datetime.strptime(request.json['InvoiceDate'], '%Y-%m-%dT%H:%M:%S'),
        request.json['BillingAddress'],
        request.json['BillingCity'],
        request.json['BillingState'],
        request.json['BillingCountry'],
        request.json['BillingPostalCode'],
        request.json['Total'])
    db.session.add(new_invoice)
    db.session.commit()
    return invoice_schema.jsonify(new_invoice)


@app.route('/api/invoices/delete/<invoice_id>', methods=['DELETE'])
def delete_invoice(invoice_id):
    Invoice.query.filter_by(InvoiceId=invoice_id).delete()
    db.session.commit()
    return "Successfully Deleted."


@app.route('/api/invoices/update/<invoice_id>', methods=['PUT', 'PATCH'])
def update_invoice(invoice_id):
    invoice = Invoice.query.filter_by(InvoiceId=invoice_id).update({
        "InvoiceId": request.json['InvoiceId'],
        "CustomerId": request.json['CustomerId'],
        "InvoiceDate": datetime.strptime(request.json['InvoiceDate'], '%Y-%m-%dT%H:%M:%S'),
        "BillingAddress": request.json['BillingAddress'],
        "BillingCity": request.json['BillingCity'],
        "BillingState": request.json['BillingState'],
        "BillingCountry": request.json['BillingCountry'],
        "BillingPostalCode": request.json['BillingPostalCode'],
        "Total": request.json['Total'],
    })
    db.session.commit()
    return "Successfully Updated!"
