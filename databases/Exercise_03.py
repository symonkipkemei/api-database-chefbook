'''
Update all films in the film table to a rental_duration value of 10,
if the length of the movie is more than 150.

'''


import sqlalchemy as s
import os
from pprint import pprint
import pymysql

#password and database
password = os.environ["MYSQL_PASSWORD"]
database_name ="sakila"

# engine, connection, metadata
engine = s.create_engine(f"mysql+pymysql://root:{password}@localhost/{database_name}")
connection = engine.connect()
metadata =s.MetaData()


#table objects
a = s.Table("actor", metadata, autoload=True, autoload_with=engine)
f = s.Table("film", metadata, autoload=True, autoload_with=engine )
fa = s.Table("film_actor",metadata, autoload=True, autoload_with=engine)
c = s.Table("category",metadata, autoload=True, autoload_with=engine)
fc = s.Table("film_category",metadata, autoload=True, autoload_with=engine)


# update films duration

#create update query

query = s.update(f).values(rental_duration=10).where(f.columns.length>50)

#excute query
result_proxy = connection.execute(query)

