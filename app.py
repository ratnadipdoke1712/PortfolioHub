from flask import Flask, render_template, request, redirect, url_for, send_file
import sqlite3

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Projects page
@app.route('/projects')
def projects():
    return render_template('projects.html')

# Resume download
@app.route('/resume')
def resume():
    return send_file('resume.pdf')

# Contact form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        conn = sqlite3.connect('contacts.db')
        cursor = conn.cursor()
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS messages (
                name TEXT,
                email TEXT,
                message TEXT
                )
            """)

        cursor.execute("""
            INSERT INTO messages (name, email, message)
            VALUES (?, ?, ?)
        """, (name, email, message))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    return render_template('contact.html')  

if __name__ == '__main__' :
    app.run(debug=True)