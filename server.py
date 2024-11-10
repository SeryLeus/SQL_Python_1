from flask import Flask
import pymysql

app = Flask(__name__)
connection = pymysql.connect(host='localhost',
                                user='root',
                                database='shop',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

def get_list_of_goods(good_type):
    list_of_good: str = ""
    try:   
        with connection.cursor() as cursor:
            sql = "select * from goods where good_type = '{}'".format(good_type)
            cursor.execute(sql)
            list_of_good = cursor.fetchall()
    except:
        list_of_good = "Sorry, we have problem with our inner data base. Try later again."
    
    return list_of_good

@app.route('/books')
def get_books():
    return get_list_of_goods('books')

@app.route('/toys')
def get_toys():
    return get_list_of_goods('toys')

def main():
    app.run()
    connection.close()

if __name__ == '__main__':
    main()
