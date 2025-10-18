
from flask import Flask, render_template
from .db import inventory_db

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home/index.html')

@app.route('/inventory')
def inventory():
    inventory = inventory_db.get_inventory()
    print(inventory)
    return render_template('inventory/index.html', inventory=inventory)

if __name__ == '__main__':
    app.run()