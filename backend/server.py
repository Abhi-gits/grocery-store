from flask import Flask, request, jsonify
from sql_connection import get_sql_connection

import products_dao
import uom_dao
import json

connection = get_sql_connection()

app = Flask(__name__)

@app.route('/getProducts')
def get_product():
    products = products_dao.get_all_product(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    #return "Hello world!" #if you want to render a .html file, 
                        # import render_template from flask and use 
                        #render_template("index.html") here.


@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)    #go to http://localhost:5000/ to view the page