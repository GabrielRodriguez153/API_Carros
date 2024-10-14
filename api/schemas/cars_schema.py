from api import ma
from marshmallow import Schema, fields

class CarsSchema(ma.Schema):
    class Meta:
        fields = ('_id','nome','modelo','ano', 'fabricante','combustivel')
    
    _id = fields.Str()
    nome = fields.Str(required=True)
    modelo = fields.Str(required=True)
    ano = fields.Str(required=True)
    fabricante = fields.Dict(required=True)
    combustivel = fields.Str(required=True)