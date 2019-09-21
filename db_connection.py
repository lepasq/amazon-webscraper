import mysql.connector
from mysql.connector import errorcode
import time
#import main

# Connecting with the MySQL Server
cnx = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              database='amazon')
cursor = cnx.cursor()

"""
# Handling of connection errors
try:
  cnx = mysql.connector.connect(user='root', 
                                password ='password', 
                                host='localhost', 
                                database='amazon')
  cursor = cnx.cursor()

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()
"""


date = time.strftime("%d %b %Y", time.gmtime())

add_airpods = ("INSERT INTO amazon.airpods "
              "VALUES (date, price)")


data_airpods = {
    'date': date,
    'price': 130#main.converted_price  <--130 is a test value
}

# Insert in airpods
cursor.execute(add_airpods)

# Make sure data is commited to the database
cnx.commit()
cursor.close()
cnx.close()