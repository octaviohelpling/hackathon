# Getting the provider areas from the database:

import sqlalchemy as sa
import json

# Note that log in details are missing as I don't want to expose them.
# I am also connecting to the wrong database.


engine = sa.create_engine('postgresql://' + details['username'] + ':' + details['password'] +'@10.15.0.1/hassle') 

# Creating the queries for the provider availabilities:
con = engine.connect()

query = """
    SELECT 
        pa.user_id,
        pc.name
    FROM 
        provider_areas pa
        JOIN postcodes pc on pa.postcode_id = pc.id
    WHERE
        pc.country = 'France'
"""

provider_areas = con.execute(query)

con.close()

# Finally putting the data into a nice JSON format.

providers = []
locations = []

for row in provider_areas:
    providers.append( row[0] )
    locations.append(row[1])
    
pairs = list(zip(providers, locations))

provider_list_of_areas = {}

for i,j in pairs:
    provider_list_of_areas.setdefault(i,[]).append(j)
    
providers_areas_json = json.dumps(provider_list_of_areas)

# End then pushing it through the API.
# To be done.


