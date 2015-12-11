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
SELECT
	user_id,
	starttime,
	endtime,
	'busy_time'::text as reason
FROM 
	busy_times bt
JOIN 
	users u on u.id = bt.id
WHERE 
	u.country = 'France'
	AND starttime >= current_date

UNION ALL

SELECT
    user_id,
    start as starttime,
    finish as endtime,
    'holiday' as reason
FROM 
    holidays h
JOIN 
	users u on u.id = h.id
WHERE 
	u.country = 'France'
	AND start >= current_date

UNION ALL 

SELECT 
    provider_user_id AS user_id,
    starttime,
    endtime,
    'event' as reason
FROM 
    events e 
JOIN 
	users u on e.provider_user_id = u.id
WHERE 
    NOT cancelled
    AND u.country = 'France'
	AND starttime >= current_date
"""

provider_unavailable_times = con.execute(query)

con.close()

# Putting the data into JSON

providers = []
starttimes = []
endtimes = []
reasons = []

for row in provider_unavailable_times:
    providers.append( row[0] )
    starttimes.append( datetime.datetime.isoformat(row[1]))
    endtimes.append( datetime.datetime.isoformat(row[2]))
    reasons.append(row[3])
    
information = list(zip(starttimes, endtimes, reasons))
unvailable_data = list(zip(providers, information))

provider_list_of_unvailable_times = {}

for i,j in unvailable_data:
    provider_list_of_unvailable_times.setdefault(i,[]).append(j)
    
providers_unvailable_json = json.dumps(provider_list_of_unvailable_times)