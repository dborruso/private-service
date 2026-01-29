import os
from flask import Flask, jsonify
from supabase import create_client, Client

app = Flask(__name__)

supabase: Client = create_client(
    os.environ.get("SUPABASE_URL"),
    os.environ.get("SUPABASE_PUBLISHABLE_KEY")
)

@app.route('/api/test')
def test():
    response = supabase.table('instruments').select("*").execute()
    instruments = response.data
    return jsonify(instruments)