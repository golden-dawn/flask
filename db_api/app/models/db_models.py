from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Equity(db.Model):
    __tablename__ = 'equities'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ticker = db.Column(db.String())
    name = db.Column(db.String())
    family = db.Column(db.String())
    exchange_id = db.Column(db.Integer, db.ForeignKey('exchanges.id'),
                            index=True)
    eod_data = db.relationship('EOD', backref='equities', lazy=True)
    id_data = db.relationship('Intraday', backref='equities', lazy=True)
    options = db.relationship('Option', backref='equities', lazy=True)
    spots = db.relationship('OptSpot', backref='equities', lazy=True)
    dividends = db.relationship('Dividend', backref='equities', lazy=True)
    

class Exchange(db.Model):
    __tablename__ = 'exchanges'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String())
    holidays = db.relationship('Holiday', backref='exchanges', lazy=True)
        

class EOD(db.Model):
    __tablename__ = 'eods'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, index=True)
    o = db.Column(db.Numeric())
    h = db.Column(db.Numeric())
    l = db.Column(db.Numeric())
    c = db.Column(db.Numeric())
    volume = db.Column(db.Integer)
    open_interest = db.Column(db.Integer)
    equity_id = db.Column(db.Integer, db.ForeignKey('equities.id'), index=True)


class Intraday(db.Model):
    __tablename__ = 'intradays'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    datetime = db.Column(db.DateTime, index=True)
    o = db.Column(db.Numeric())
    h = db.Column(db.Numeric())
    l = db.Column(db.Numeric())
    c = db.Column(db.Numeric())
    volume = db.Column(db.Integer)
    open_interest = db.Column(db.Integer)
    equity_id = db.Column(db.Integer, db.ForeignKey('equities.id'), index=True)


class Option(db.Model):
    __tablename__ = 'options'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, index=True)
    und = db.Column(db.Integer, db.ForeignKey('equities.id'), index=True)
    expiry = db.Column(db.Date, index=True)
    cp = db.Column(db.String(1))
    strike = db.Column(db.Numeric())
    bid = db.Column(db.Numeric())
    ask = db.Column(db.Numeric())
    volume = db.Column(db.Integer)

    
class OptSpot(db.Model):
    __tablename__ = 'opt_spots'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, index=True)
    spot = db.Column(db.Numeric())
    equity_id = db.Column(db.Integer, db.ForeignKey('equities.id'), index=True)


class Dividend(db.Model):
    __tablename__ = 'dividends'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, index=True)
    ratio = db.Column(db.Float)
    divi_type = db.Column(db.SmallInteger)
    equity_id = db.Column(db.Integer, db.ForeignKey('equities.id'), index=True)


class Holiday(db.Model):
    __tablename__ = 'holidays'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String())
    date = db.Column(db.Date, index=True)
    exchange_id = db.Column(db.Integer, db.ForeignKey('exchanges.id'),
                            index=True)
