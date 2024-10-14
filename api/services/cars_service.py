from api import mongo
from ..models import cars_model
from bson import ObjectId

class CarsService:
    def add_car(car):
        result = mongo.db.cars.insert_one({
            'nome' : car.nome,
            'modelo' : car.modelo,
            'ano' : car.ano,
            'fabricante' : car.fabricante,
            'combustivel' : car.combustivel
        })
        return mongo.db.cars.find_one({'_id': ObjectId(result.inserted_id)})
    
    @staticmethod
    def get_cars():
        return list(mongo.db.cars.find())
    
    @staticmethod
    def get_cars_by_id(id):
        return mongo.db.cars.find_one({'_id': ObjectId(id)})
    
    @staticmethod
    def update_cars(self, id):
        updated_cars = mongo.db.cars.find_one_and_update(
            {'_id': ObjectId(id)},
            {'$set':{
                'nome' : self.nome,
                'modelo' : self.modelo,
                'ano': self.ano,
                'fabricante': self.fabricante,
                'combustivel': self.combustivel
            }},
            return_document=True
        )
    
    @staticmethod
    def delete_cars(id):
        mongo.db.cars.delete_one({'_id': ObjectId(id)})