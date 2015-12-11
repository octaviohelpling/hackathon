-- Example of getting the provider availabilities from H2 database

-- LOCATIONS:

SELECT 
    user_id,
    pc.name as postcode_name
FROM 
    provider_areas pa
    JOIN postcodes pc on pa.postcode_id = pc.id
WHERE
    pc.country = 'France' ;

    
-- AVAILABILITIES    

-- Time, when not available.

SELECT
	user_id,
	starttime,
	endtime
FROM 
	busy_times bt
JOIN 
	users u on u.id = bt.id
WHERE 
	u.country = 'France' 
    and starttime >= current_date;

/*
SELECT
    h.*
FROM 
    holidays h
JOIN 
	users u on u.id = h.id
WHERE 
	u.country = 'France' ;
*/


SELECT 
    provider_user_id,
    starttime,
    endtime,
    cancelled
FROM 
    events e 
JOIN 
	users u on e.provider_user_id = u.id
WHERE 
    u.country = 'France'
	and starttime >= current_date;



-- FINALLY THE AVAILABLE TIMES OF THE PROVIDERS


SELECT
    user_id,
    day,
    open_time,
    close_time,
    available
FROM 
    working_hours ;

