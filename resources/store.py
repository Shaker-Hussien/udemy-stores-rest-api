from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):

    def get(self, name):
        store = StoreModel.get_store_by_name(name)
        return store.json() if store else {'message': 'No Store found with this name.'}, 404

    def post(self, name):
        existing_store = StoreModel.get_store_by_name(name)
        if existing_store:
            return {'message': 'Store already exists with same Name'}, 400

        new_store = StoreModel(name)

        return new_store.upsert(), 201

    def delete(self, name):
        store = StoreModel.get_store_by_name(name)
        if not store:
            return {'message': 'Store Not found'}, 404

        store.delete()
        return {'message': f'store with name {name} deleted successfully'}


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
