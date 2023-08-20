import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
import json
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

jackson_family = FamilyStructure("Jackson")

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<int:id>', methods=['GET'])
def get_member(id):
    member = jackson_family.get_member(id)
    if member:
        response = {
            "name": f"{member['first_name']} {jackson_family.last_name}",
            "age": member["age"],
            "lucky_numbers": member["lucky_numbers"],
            "id": member["id"]
        }
        json_response = json.dumps(response, indent=4)  # Convertir a JSON manualmente
        return json_response, 200, {'Content-Type': 'application/json'}
    else:
        return jsonify({"message": "Member not found"}), 404


@app.route('/member', methods=['POST'])
def add_member():
    request_data = request.json
    member_id = jackson_family.add_member(request_data)
    return jsonify({"message": "Member added", "id": member_id}), 200

@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    if jackson_family.delete_member(id):
        return jsonify({"done": True}), 200
    else:
        return jsonify({"message": "Member not found"}), 404


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
