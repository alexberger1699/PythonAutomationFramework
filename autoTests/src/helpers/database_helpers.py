import pymysql


def read_from_db(sql):
    #connect to db
    connection = pymysql.connect(host = '127.0.0.1', port= 8889, user = 'root', password= 'root' )
    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        db_data = cursor.fetchall()
        cursor.close()
    finally:
        connection.close()

    #return the results from db
        return db_data

def get_order_from_db_by_order_no(order_no):
    sql = f"SELECT * FROM quicksitedb.wp_posts where id = 60 and post_type = 'shop_coupon';"
    db_order = read_from_db(sql)
    print(db_order)

get_order_from_db_by_order_no(60)