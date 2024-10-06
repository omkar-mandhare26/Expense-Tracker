from flask import Flask, request, render_template
from dotenv import load_dotenv
from database import mySQLdatabase
import os

app = Flask(__name__)
db = mySQLdatabase()

@app.route('/')
def index():
    DB_data = db.getAllExpenses()
    sum = 0
    for exp in DB_data:
        sum+= exp["amount"]

    return render_template('index.html',data = DB_data,total_amount = sum)

@app.route('/addpositions')
def add():
    return render_template('addpositions.html')

@app.route('/insertdata',methods=['GET'])
def insert():
    name = request.args.get('name')
    price = request.args.get('price')

    if not name or not price:
        return "Invalid input", 400

    try:
        price = float(price)
    except ValueError:
        return "Invalid price", 400

    db.addExpense(name, price)
    return "Expense added successfully", 200

@app.route('/deleteallDB',methods=['POST'])
def deleteAll():
    db.deleteAll()
    return "All records deleted", 200


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello, {name}!'
    elif request.method == 'GET':
        name = request.args.get('name')
        return f'Hello, {name}!'
    return 'Invalid Request'

if __name__ == '__main__':
    app.run(debug=True)
