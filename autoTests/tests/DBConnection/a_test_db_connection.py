import time
import pymysql

def read_from_db(sql):
    #connect to DB
    connection = pymysql.connect(host="127.0.0.1", user="alex.db",
                                 password="7663598", database="autodb")
##


    #read

    #return the result
    return db_data


def get_order_from_db_order_no():
    sql = f"SELECT * FROM PersonCodes"
    db_order = read_from_db(sql)
    print(db_order)

read_from_db()






































def connect_to_db():
    """
    התחבר לבסיס נתונים

    :return: חיבור לבסיס נתונים
    """

    conn = pymysql.connect(
        host="fuelpointqa.database.windows.net",
        user="yoni",
        password="Pooh2357",
        database="Fuel_Web_Dev_India_QA"
    )
    return conn

def disconnect_from_db(conn):
    """
    ניתוק מהבסיס נתונים

    :param conn: חיבור לבסיס נתונים
    """

    conn.close()

def main():
    """
    בדיקת חיבור לבסיס נתונים
    """

    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("Select * from PersonCodes")
    result = cursor.fetchone()
    if result is not None:
        print("חיבור לבסיס נתונים הצליח")
    else:
        print("חיבור לבסיס נתונים נכשל")
    disconnect_from_db(conn)

if __name__ == "__main__":
    main()
