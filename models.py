from sqlalchemy.dialects.postgresql import HSTORE
from sqlalchemy.ext.mutable import MutableDict
from app import   DB

class Word_emddings(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(80), nullable=False, unique=True)
    stats = DB.Column(MutableDict.as_mutable(HSTORE))