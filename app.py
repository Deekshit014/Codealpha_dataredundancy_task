from flask import Flask, request, jsonify, send_from_directory
from utils import generate_hash, load_local_db, save_local_db
import os

app = Flask(__name__, static_folder='static', static_url_path='/static')
LOCAL_DB = os.path.join(os.path.dirname(__file__), "local_db.json")

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/add', methods=['POST'])
def add_record():
    try:
        data = request.get_json(force=True)
        if not isinstance(data, dict):
            return jsonify({"status":"error","message":"JSON object expected"}),400

        record_hash = generate_hash(data)
        db = load_local_db()

        if record_hash in db:
            return jsonify({"status":"duplicate","message":"Redundant data detected (local)!"}),409

        data_with_hash = dict(data)
        data_with_hash["hash"] = record_hash
        db[record_hash] = data_with_hash
        save_local_db(db)
        return jsonify({"status":"success","message":"Unique data added to local storage!"}),201

    except Exception as e:
        return jsonify({"status":"error","message":str(e)}),500

@app.route('/all', methods=['GET'])
def get_all():
    db = load_local_db()
    return jsonify(list(db.values())), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
