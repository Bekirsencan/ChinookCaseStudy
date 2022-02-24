from app import db
from app import ma


class Invoice(db.Model):
    __tablename__ = 'invoices'
    InvoiceId = db.Column(db.Integer, primary_key=True, nullable=False)
    CustomerId = db.Column(db.Integer, nullable=False)
    InvoiceDate = db.Column(db.DateTime, nullable=False)
    BillingAddress = db.Column(db.String(70))
    BillingCity = db.Column(db.String(40))
    BillingState = db.Column(db.String(40))
    BillingCountry = db.Column(db.String(40))
    BillingPostalCode = db.Column(db.String(10))
    Total = db.Column(db.Numeric(10, 2), nullable=False)

    def __init__(self, CustomerId, InvoiceDate, BillingAddress, BillingCity, BillingState, BillingCountry,
                 BillingPostalCode, Total):
        self.CustomerId = CustomerId
        self.InvoiceDate = InvoiceDate
        self.BillingAddress = BillingAddress
        self.BillingCity = BillingCity
        self.BillingState = BillingState
        self.BillingCountry = BillingCountry
        self.BillingPostalCode = BillingPostalCode
        self.Total = Total


class InvoiceSchema(ma.Schema):
    class Meta:
        fields = (
            "InvoiceId", "CustomerId", "InvoiceDate", "BillingAddress", "BillingCity", "BillingState", "BillingCountry",
            "BillingPostalCode", "Total")


invoices_schema = InvoiceSchema(many=True)
invoice_schema = InvoiceSchema()
