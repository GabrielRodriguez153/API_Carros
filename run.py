from api import app, mongo
from api.models.cars_model import Cars
from api.services.cars_service import CarsService

if __name__ == '__main__':
    with app.app_context():
        if 'cars' not in mongo.db.list_collection_names():
            cars = Cars(
                nome = '',
                modelo = '',
                ano = 0,
                fabricante = '',
                combustivel = ''
            ) 
            CarsService.add_car(cars)
    app.run(port=5000, debug=True)