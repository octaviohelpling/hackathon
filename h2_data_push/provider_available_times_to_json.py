# Getting the provider available and unavailable times to JSON

# Getting the provider areas from the database:

import sqlalchemy as sa
import json
import datetime

# Note that log in details are missing as I don't want to expose them.
# I am also connecting to the wrong database.

engine = sa.create_engine('postgresql://' + details['username'] + ':' + details['password'] +'@10.15.0.1/hassle') 

# Creating the queries for the provider availabilities:

con = engine.connect()

query = """
WITH next_days as (
	SELECT
	generate_series(CURRENT_DATE, (CURRENT_DATE + INTERVAL '30 days')::DATE, '1 days') as date)

SELECT
	user_id,
	date + open_time as starttime,
	date + close_time as endtime
FROM 
	next_days nd
	JOIN working_hours wh on extract('dow' from nd.date) = wh.day
	JOIN users u on u.id = wh.id
WHERE 
    u.country = 'France'
	AND date + open_time  >= current_date
"""

provider_available_times = con.execute(query)

con.close()

# Putting to JSON-format

providers = []
starttimes = []
endtimes = []

for row in provider_available_times:
    providers.append( row[0] )
    starttimes.append( datetime.datetime.isoformat(row[1]))
    endtimes.append( datetime.datetime.isoformat(row[2]))
    
information = list(zip(starttimes, endtimes))
available_data = list(zip(providers, information))

provider_list_of_available_times = {}

for i,j in available_data:
    provider_list_of_available_times.setdefault(i,[]).append(j)
    
providers_available_json = json.dumps(provider_list_of_available_times)