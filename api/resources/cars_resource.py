from flask_restful import Resource
from api import api
from flask import make_response,jsonify,request
from ..schemas import cars_schema
from ..models import cars_model
from ..services.cars_service import CarsService

class CarsList(Resource):
    def get(self):
        caros = CarsService.get_cars()
        caro = cars_schema.CarsSchema(many=True)
        return make_response(caro.jsonify(caros), 200)
    
    def post(self):
        carschema = cars_schema.CarsSchema()
        validate = carschema.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            json_data = request.get_json()
            new_car = cars_model.Cars(**json_data)
            result = CarsService.add_car(new_car)
            res = carschema.jsonify(result)
            return make_response(res,201)
        
class CarsDetails(Resource):
    def get(self,id):
        cars = CarsService.get_cars_by_id(id)
        if cars is None:
            return make_response(jsonify("Carro não Encontrado"),400)
        carschema = cars_schema.CarsSchema()
        return make_response(carschema.jsonify(cars), 200)
    
    def put(self, id):
        cars_bd = CarsService.get_cars_by_id(id)
        if cars_bd is None:
            return make_response(jsonify("Carro não Encontrado"), 404)
        carschema = cars_schema.CarsSchema()
        validate = carschema.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else: 
            json_data = request.get_json()
            new_car = cars_model.Cars(**json_data)
            update_car = CarsService.update_cars(new_car,id)
            return make_response(carschema.jsonify(update_car), 200)
    
    def delete(self, id):
        cars_bd = CarsService.get_cars_by_id(id)
        if cars_bd is None:
            return make_response(jsonify("Carro não Encontrado"), 404)
        CarsService.delete_cars(id)
        return make_response(jsonify("Carro Excluído com Sucesso"), 200)
        

api.add_resource(CarsList, '/cars')
api.add_resource(CarsDetails, '/cars/<id>')