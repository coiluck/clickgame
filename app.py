from flask import Flask, render_template, jsonify, request
import sqlite3
import os

app = Flask(__name__)

DB_FILE = "database.db"

# データベース初期化
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS counter (id INTEGER PRIMARY KEY, count INTEGER)''')
    c.execute("INSERT OR IGNORE INTO counter (id, count) VALUES (1, 0)")
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/click', methods=['POST'])
def click():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("UPDATE counter SET count = count + 1 WHERE id = 1")
    conn.commit()
    c.execute("SELECT count FROM counter WHERE id = 1")
    count = c.fetchone()[0]
    conn.close()
    return jsonify({'count': count})

@app.route('/get_count')
def get_count():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT count FROM counter WHERE id = 1")
    count = c.fetchone()[0]
    conn.close()
    return jsonify({'count': count})

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
