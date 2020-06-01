from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="help for price"
                        )

    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="help for store_id"
                        )

    @jwt_required()
    def get(self, name):
        item = ItemModel.get_item_by_name(name)
        return item.json() if item else {'message': 'No item found'}, 404

    def post(self, name):
        old_item = ItemModel.get_item_by_name(name)
        if ItemModel.get_item_by_name(name):
            return {'message': f'item already exists with data {old_item}'}, 400

        data = Item.parser.parse_args()
        new_item = ItemModel(name, **data)

        return new_item.upsert(), 201

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        new_item = ItemModel(name, **data)

        # insert item if not found
        existed_item = ItemModel.get_item_by_name(name)
        if not existed_item:
            return new_item.upsert(), 201

        existed_item.price = data['price']
        existed_item.price = data['store_id']
        return existed_item.upsert()

    @jwt_required()
    def delete(self, name):
        item = ItemModel.get_item_by_name(name)
        if not item:
            return {'message': 'Not found'}, 404

        item.delete()
        return {'message': f'item with name {name} deleted successfully'}


class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
