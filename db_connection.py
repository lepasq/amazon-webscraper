import mysql.connector
from mysql.connector import errorcode
import time
#import main

cnx = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              database='amazon')
cursor = cnx.cursor()


#handling of connection errors
try:
  cnx = mysql.connector.connect(user='root',
                                database='amazon')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()


date = time.strftime("%d %b %Y", time.gmtime())

def insert_date():
    add_date = ("INSERT INTO amazon.airpods "
                "VALUES (date, price)")


data_airpods = {
    'date': date#,
#    'price': converted_price
# does not work yet, since the main file is not imported yet
}