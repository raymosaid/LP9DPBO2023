import mysql.connector
 
# connecting to the mysql server
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "db_latihan9_dpbo"
)

# Insert
dbcursor = mydb.cursor()

sql = "INSERT INTO t_address (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
dbcursor.execute(sql, val)

mydb.commit()
print(dbcursor.rowcount, "record inserted")

sql = "INSERT INTO t_address (name, address) VALUES (%s, %s)"
val = ("David", "102 Street")
dbcursor.execute(sql, val)

mydb.commit()
print(dbcursor.rowcount, "record inserted")

# Select
dbcursor = mydb.cursor()

dbcursor.execute("SELECT * FROM t_address")

myresult = dbcursor.fetchall()

for x in myresult:
    print(x)

# Delete
dbcursor = mydb.cursor()

sql = "Delete FROM t_address WHERE address = 'Highway 21'"
dbcursor.execute(sql)

mydb.commit()
print(dbcursor.rowcount, "record(s) deleted")
