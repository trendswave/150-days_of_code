import sys
import MySQLdb

# Extracting command-line arguments
mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]
state_name = sys.argv[4]

# Connecting to the MySQL server
db = MySQLdb.connect(
    host='localhost',
    port=3306,
    user=mysql_username,
    passwd=mysql_password,
    db=database_name
)

# Creating a cursor object to execute SQL queries
cursor = db.cursor()

# Creating the SQL query using user input
query = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(
    state_name)

# Executing the query
cursor.execute(query)

# Fetching all the rows returned by the query
rows = cursor.fetchall()

# Displaying the results
for row in rows:
    print(row)

# Closing the cursor and database connection
cursor.close()
db.close()
