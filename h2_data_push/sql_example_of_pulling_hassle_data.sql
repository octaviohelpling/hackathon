-- Example of getting the provider availabilities from H2 database

-- LOCATIONS:

SELECT 
    pa.user_id,
    pc.name
FROM 
    provider_areas pa
    JOIN postcodes pc on pa.postcode_id = pc.id
WHERE
    pc.country = 'France'

    
-- AVAILABILITIES    

-- Time, when not available.

-- busy times 
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



-- FINALLY THE AVAILABLE TIMES OF THE PROVIDERS

select
user_id,
day,
open_time,
close_time
from working_hours
where available
limit 1000
