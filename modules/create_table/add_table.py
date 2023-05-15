import sqlite3

#What is DB name??
db_name='products.db'
#What is your table name??
table_name='inventory' 
db = sqlite3.connect(db_name)
cur = db.cursor()
# id is the primary key for the table: 
# you can change if necessary.
# change Column_2 and rest according to your requiremenst
# change data type accordingly (REAL ,TEXT, INTEGER)
# if it shouln't be empty marked with 'NOT NULL' as below.

cur.execute("""
CREATE TABLE IF NOT EXISTS {table_name} (
    id INTEGER PRIMARY KEY,
    column_2 REAL NOT NULL,
    column_3 TEXT,
    column_4 TEXT,
    column_5 INTEGER
    column_6 TEXT
)
""")

db.commit()
db.close()




