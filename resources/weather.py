from flask_restful import Resource, reqparse
from flask import request
from home_back.models.weather import City, WeatherData, WeatherConfig

class Weather(Resource):
    def get(self):
        # TODO: get all weather data from database
        cities = City.query.all()
        
        return {'cities': [ city.to_dict() for city in cities ]}, 201

    def post(self):
        # TODO: save new City name
        data = request.get_json()

        if data:
            city = City(
                city_name=data['city_name'],
                country_code=data['country_code']
            )

    def put(self, city_name):
        # TODO: save one new or update an existing city
        pass

class WeatherPrefs(Resource):
    def get(self):
        config = WeatherConfig.get_config()

        return {'weather_config': config.to_dict() }

    def post(self):
        data = request.get_json()

        if data:
            config = WeatherConfig(
                api_key=data['api_key']
            )

            try:
                config.save()
            except:
                return {'message': 'An error occured while inserting to db'}, 500

            return {'weather_config': config.to_dict() }, 201

    def put(self):
        data = request.get_json()

        config = WeatherConfig.query.filter_by(api_key=data['api_key']).first()

        if config is None:
            config = WeatherConfig(
                api_key=data['api_key']
            )
        else:
            config.api_key = data['api_key']

        config.save()

        return {'weather_config': config.to_dict() }, 201
