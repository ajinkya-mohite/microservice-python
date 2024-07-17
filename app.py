from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from pymongo import MongoClient
from config import Config
from bson.objectid import ObjectId

app = Flask(__name__)
app.config.from_object(Config)

api = Api(app)
jwt = JWTManager(app)

client = MongoClient(app.config['MONGO_URI'])
db = client.mydatabase
collection = db.mycollection

@app.route('/login', methods=['POST'])
def login():
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        if username != 'test' or password != 'test':
            return jsonify({"msg": "Bad username or password"}), 401

        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)

class Item(Resource):
        @jwt_required()
        def get(self, item_id):
            item = collection.find_one({"_id": ObjectId(item_id)})
            if item:
                item['_id'] = str(item['_id'])  # Convert ObjectId to string
                return jsonify(item)
            return {"message": "Item not found"}, 404

        @jwt_required()
        def post(self):
            data = request.get_json()
            result = collection.insert_one(data)
            return {"message": "Item created", "id": str(result.inserted_id)}, 201

        @jwt_required()
        def put(self, item_id):                    
            data = request.get_json()                       
            result = collection.update_one({"_id": ObjectId(item_id)}, {"$set": data})                          
            if result.matched_count:
                return {"message": "Item updated"}, 200                                                     
            return {"message": "Item not found"}, 404

        @jwt_required()              
        def delete(self, item_id):
           result = collection.delete_one({"_id": ObjectId(item_id)})               
           if result.deleted_count:                                 
               return {"message": "Item deleted"}, 200
           return {"message": "Item not found"}, 404

class HealthCheck(Resource):
    def get(self):
        return {"status": "healthy"}, 200
             

api.add_resource(Item, '/item', '/item/<string:item_id>')                           
api.add_resource(HealthCheck, '/health')

@app.errorhandler(404)
def not_found(error):                       
    return jsonify({"message": "Not found"}), 404 
                                                                               
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"message": "Internal server error"}), 500

                                                                           
if __name__ == '__main__':
    app.run(debug=True)
