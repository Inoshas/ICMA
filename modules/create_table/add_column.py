import sqlite3

#What is DB name??
db_name='' # DB name goes here 
#What is your table name??
table_name=''  # Tablename goes here
column_name ='' # column name goes here
data_type='' # Datatype goes here

db = sqlite3.connect(db_name)
cur = db.cursor()

### if you want to add more colums to table use this
cur.execute(""" ALTER TABLE {table_name}}
    ADD COLUMN {column_name} {Data_type} """)



db.commit()
db.close()




