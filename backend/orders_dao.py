from sql_connection import get_sql_connection
from datetime import datetime


def insert_order(connection, order):
    cursor = connection.cursor()
     
    #insert order
    order_query = ("INSERT INTO order (customer_name, total_cost, datetime) VALUES (%s, %s,%s)")  # datetime.now()
    order_data = (order['customer_name'], order['grand_total'], order['datetime'])
    cursor.execute(order_query, order_data)
    order_id = cursor.lastrowid
    
    order_details_query = ("INSERT INTO order_detail (order_id, product_id, quantity, total_price) VALUES (%s, %s, %s, %s)")
    
    #insert order details
    order_detail_data = []
    for order_detail_record in order['order_detail']:
        order_detail_data.append([ 
            order_id,
            int(order_detail_record['product_id']),
            float(order_detail_record['quantity']),
            float(order_detail_record['total_price'])
        ]) 
    
    cursor.executemany(order_details_query, order_detail_data)
    
    connection.commit()
    return order_id


if __name__ == '__main__':
    connection = get_sql_connection()
    print(insert_order(connection, {
        'customer_name': 'codebasics',
        'grand_total': 500,
        'datetime': datetime.now(),
        'order_detail': [
            {
                'product_id': 1,
                'quantity': 2,
                'total_price': 50
            },
            {
                'product_id': 3,
                'quantity': 2,
                'total_price': 30
            }
        ]
        
    }))
    