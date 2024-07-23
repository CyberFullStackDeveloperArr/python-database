import mysql.connector
from mysql.connector import Error

def get_connection():
   try: 
      connection = mysql.connector.connect(
         host='localhost',
         database='py_database',
         user='root',
         password=''
      )

      if connection.is_connected():
         print("Python Terhubung Database!")
         return connection

   except Error as e:
     print(f"Error Python Terhubung!: {e}")
     return None


def read_admin_names():
   connection = get_connection()
   if connection:
      try:
         cursor = connection.cursor()
         cursor.execute("SELECT nama FROM admin")
         rows = cursor.fetchall()
         for row in rows:
            print(row[0])
      except Error as e:
         print(f"Error saat membaca data: {e}")
      finally:
         cursor.close()
         connection.close()
           
read_admin_names()

