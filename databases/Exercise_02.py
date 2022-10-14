'''
Consider each of the tasks below as a separate database query. Using SQLAlchemy, which is the necessary code to:

- Select all the actors with the first name of your choice

- Select all the actors and the films they have been in

- Select all the actors that have appeared in a c of a comedy of your choice

- Select all the comedic films and sort them by rental rate

- Using one of the statements above, add a GROUP BY statement of your choice

- Using one of the statements above, add a ORDER BY statement of your choice

'''

from itertools import count
from unittest import result
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


# Select all the actors with the first name of your choice
#__________________________________________________________


query_1 = s.select([a]).where(a.columns.first_name=="harrison")

# execute query
result_proxy = connection.execute(query_1)

#fetch results
results = result_proxy.fetchall()

#print(results)


#Select all the actors and the films they have been in
#__________________________________________________________


#join a and f table using join query
join_statement = a.join(fa, fa.columns.actor_id == a.columns.actor_id).join(f,f.columns.film_id == fa.columns.film_id)
join_query = s.select([a.columns.first_name,a.columns.last_name,f.columns.title]).select_from(join_statement)

#execute query
result_proxy = connection.execute(join_query)

for result in result_proxy:
    pass
    #print(result)


#Select all the actors that have appeared in a c of a comedy of your choice
#__________________________________________________________

#join (a>>fa>>f>>f-c>>c)

join_statement_2 = a.join(fa, fa.columns.actor_id == a.columns.actor_id).join(f,f.columns.film_id==fa.columns.film_id).join(fc,fc.columns.film_id == f.columns.film_id).join(c,fc.columns.category_id==c.columns.category_id)
join_query_2 = s.select([a.columns.first_name,a.columns.last_name,c.columns.name]).select_from(join_statement_2).where(c.columns.name == "Action")

result_proxy = connection.execute(join_query_2)

#fetch from results
for y in result_proxy:
    pass
    #print(y)

#Select all the comedic films and sort them by rental rate
#__________________________________________________________
# Tables involved : film, film_category, category

join_statement_3 = f.join(fc,fc.columns.film_id==f.columns.film_id).join(c,c.columns.category_id==fc.columns.category_id)
join_query_3 = s.select([f.columns.title]).select_from(join_statement_3).where(c.columns.name=="comedy").order_by(s.asc(f.columns.rental_rate))

#execute query
result_proxyy = connection.execute(join_query_3)

for result in result_proxyy:
    pass
    #print(result[0])





# Using one of the statements above, add a GROUP BY statement of your choice
# aggregate how many actors have participated in which category of film

join_statement_2 = a.join(fa, fa.columns.actor_id == a.columns.actor_id).join(f,f.columns.film_id==fa.columns.film_id)
join_query_4 = s.select([a.columns.first_name,a.columns.last_name,s.func.count(a.columns.actor_id)]).select_from(join_statement_2).group_by(a.columns.actor_id)

result_proxy = connection.execute(join_query_4)

for x in result_proxy:
    pass
    #print(x)



#- Using one of the statements above, add a ORDER BY statement of your choice
#_____________________________________________________________________________
join_statement_2 = a.join(fa, fa.columns.actor_id == a.columns.actor_id).join(f,f.columns.film_id==fa.columns.film_id)
join_query_4 = s.select([a.columns.first_name,a.columns.last_name,s.func.count(a.columns.actor_id)]).select_from(join_statement_2).group_by(a.columns.actor_id).order_by(s.asc(a.columns.first_name))

result_proxy = connection.execute(join_query_4)

for x in result_proxy:
    print(x)


