from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Equity(db.Model):
    __tablename__ = 'equities'
    ticker = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String())
    family = db.Column(db.String())
    exchange = db.Column(db.String(), db.ForeignKey('exchanges.name'),
                         index=True)
    eod_data = db.relationship('EOD', backref='equities', lazy=True)
    id_data = db.relationship('Intraday', backref='equities', lazy=True)
    options = db.relationship('Option', backref='equities', lazy=True)
    spots = db.relationship('OptSpot', backref='equities', lazy=True)
    dividends = db.relationship('Dividend', backref='equities', lazy=True)


class Exchange(db.Model):
    __tablename__ = 'exchanges'
    name = db.Column(db.String(), primary_key=True)
    holidays = db.relationship('Holiday', backref='exchanges', lazy=True)


class EOD(db.Model):
    __tablename__ = 'eods'
    date = db.Column(db.Date, primary_key=True)
    stk = db.Column(db.String(), db.ForeignKey('equities.ticker'),
                    primary_key=True)
    o = db.Column(db.Numeric())
    hi = db.Column(db.Numeric())
    lo = db.Column(db.Numeric())
    c = db.Column(db.Numeric())
    volume = db.Column(db.Integer)
    open_interest = db.Column(db.Integer)


class Intraday(db.Model):
    __tablename__ = 'intradays'
    datetime = db.Column(db.DateTime, primary_key=True)
    stk = db.Column(db.String(), db.ForeignKey('equities.ticker'),
                    primary_key=True)
    o = db.Column(db.Numeric())
    hi = db.Column(db.Numeric())
    lo = db.Column(db.Numeric())
    c = db.Column(db.Numeric())
    volume = db.Column(db.Integer)
    open_interest = db.Column(db.Integer)


class Option(db.Model):
    __tablename__ = 'options'
    date = db.Column(db.Date, primary_key=True)
    und = db.Column(db.String(), db.ForeignKey('equities.ticker'),
                    primary_key=True)
    expiry = db.Column(db.Date, primary_key=True)
    cp = db.Column(db.String(1), primary_key=True)
    strike = db.Column(db.Numeric(), primary_key=True)
    bid = db.Column(db.Numeric())
    ask = db.Column(db.Numeric())
    volume = db.Column(db.Integer)


class OptSpot(db.Model):
    __tablename__ = 'opt_spots'
    date = db.Column(db.Date, primary_key=True)
    stk = db.Column(db.String(), db.ForeignKey('equities.ticker'),
                    primary_key=True)
    spot = db.Column(db.Numeric())


class Dividend(db.Model):
    __tablename__ = 'dividends'
    date = db.Column(db.Date, primary_key=True)
    stk = db.Column(db.String(), db.ForeignKey('equities.ticker'),
                    primary_key=True)
    ratio = db.Column(db.Float)
    divi_type = db.Column(db.SmallInteger)


class Holiday(db.Model):
    __tablename__ = 'holidays'
    date = db.Column(db.Date, primary_key=True)
    exchange = db.Column(db.String(), db.ForeignKey('exchanges.name'),
                         primary_key=True)
    name = db.Column(db.String())
