class Account(db.Model):
    acc_num = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50))
    transaction_details = db.Column(db.String(255))
    value_date = db.Column(db.String(50))
    deposit_amt = db.Column(db.Strint(50))
    balance_amt = db.Column(db.Strint(50))

    def __repr__(self):
        return '<Account %s>' % self.acc_num