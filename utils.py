import hashlib, json, os
LOCAL_DB_PATH = os.path.join(os.path.dirname(__file__), "local_db.json")

def generate_hash(record):
    # produce a stable hash ignoring key order
    record_str = json.dumps(record, sort_keys=True, separators=(',',':'))
    return hashlib.sha256(record_str.encode('utf-8')).hexdigest()

def load_local_db():
    if not os.path.exists(LOCAL_DB_PATH):
        return {}
    with open(LOCAL_DB_PATH, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except Exception:
            return {}

def save_local_db(db_dict):
    with open(LOCAL_DB_PATH, 'w', encoding='utf-8') as f:
        json.dump(db_dict, f, indent=2, ensure_ascii=False)
