'''

All of the following exercises should be done using sqlalchemy.

Using the provided database schema, write the necessary code to print information about the film and category table.

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


# create table objects to be used
film = s.Table("film", metadata, autoload=True, autoload_with=engine)
actor = s.Table("actor", metadata, autoload=True, autoload_with=engine)


#query 
film_query = s.select([film])
actor_query = s.select([actor])

# execute query
result_proxy_film = connection.execute(film_query)
result_proxy_category = connection.execute(actor_query)


pprint(result_proxy_category.fetchmany(5))

print("**********BREAK***************")
pprint(result_proxy_film.fetchmany(5))


