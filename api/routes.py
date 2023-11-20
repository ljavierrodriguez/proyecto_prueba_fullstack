from flask import Blueprint, jsonify, request
from models import User

api = Blueprint("api", __name__)

@api.route('/users', methods=['GET'])
def get_users():
    
    users = User.query.all()
    users = list(map(lambda user: user.serialize(), users))
    
    return jsonify(users), 200
    