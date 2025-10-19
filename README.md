# CodeAlpha - Data Redundancy Removal System 

## Overview
This project demonstrates a Data Redundancy Removal System using local JSON storage.
It accepts JSON records via a REST API, generates a SHA-256 hash per record,
and prevents duplicate entries from being stored (local fallback mode).

## Quick start (local)
1. Create and activate virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Run the Flask app:
   ```
   python app.py
   ```

3. Open the frontend in your browser:
   http://127.0.0.1:5000

4. (Optional) Use Streamlit UI:
   ```
   streamlit run ui.py
   ```

## API
- `POST /add` : add a JSON record. Returns 201 on success, 409 if duplicate.
- `GET /all` : list stored records.

## Files
- `app.py`
- `utils.py`
- `index.html`
- `ui.py`
- `requirements.txt`
- `sample_client.sh`
- `local_db.json`

