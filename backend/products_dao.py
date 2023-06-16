# dao -> data access object 

from sql_connection import get_sql_connection


def get_all_product(connection):
    cursor = connection.cursor()

    query = ("SELECT product.Product_id, product.Product_name, product.uom_id, product.Price_per_unit, uom.uom_name FROM product inner join uom on uom.uom_id=product.uom_id")

    cursor.execute(query)
    
    response = []

    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'name' : name,
            'uom_id' : uom_id,
            'price_per_unit' : price_per_unit,
            'uom_name' : uom_name
            })
        
    
    return response


def insert_new_product(connection, product):
    cursor = connection.cursor()
    
    query = ("INSERT INTO product ( product_name, uom_id, price_per_unit) VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    
    cursor.execute(query, data)
    connection.commit()
    
    return cursor.lastrowid


def delete_product(connection, product_id):
    cursor = connection.cursor()
    
    query = ("DELETE FROM product where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()
    
    return cursor.lastrowid
    
if __name__=='__main__':
    connection = get_sql_connection()
    #print(get_all_product(connection))
    # print(insert_new_product(connection, {
    #     'product_name': 'bracolli',
    #     'uom_id': '1',
    #     'price_per_unit': '20'    
    #     }))
    
    #print(delete_product(connection, 10))