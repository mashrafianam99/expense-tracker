from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Connect to database
def get_db_connection():
    conn = sqlite3.connect('expense.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create table if not exists
def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            category TEXT,
            date TEXT,
            note TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()

    if request.method == 'POST':
        amount = request.form['amount']
        category = request.form['category']
        date = request.form['date']
        note = request.form['note']

        conn.execute(
            "INSERT INTO expenses (amount, category, date, note) VALUES (?, ?, ?, ?)",
            (amount, category, date, note)
        )
        conn.commit()
        return redirect('/')

    expenses = conn.execute("SELECT * FROM expenses ORDER BY date DESC").fetchall()
    total = sum(exp['amount'] for exp in expenses)
    conn.close()

    return render_template('index.html', expenses=expenses, total=total)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


