-- Example of getting the provider availabilities from H2 database

-- LOCATIONS:

SELECT 
    *
FROM 
    provider_areas pa
    JOIN postcodes pc on pa.postcode_id = pc.id
WHERE
    pc.country = 'France' ;

    
-- AVAILABILITIES    

-- Time, when not available.

SELECT
	bt.*
FROM 
	busy_times bt
JOIN 
	users u on u.id = bt.id
WHERE 
	u.country = 'France' ;


SELECT
    h.*
FROM 
    holidays h
JOIN 
	users u on u.id = h.id
WHERE 
	u.country = 'France' ;



SELECT 
    e.*
FROM 
    events e 
JOIN 
	users u on e.provider_user_id = u.id
WHERE 
    u.country = 'France' ;



-- FINALLY THE AVAILABLE TIMES OF THE PROVIDERS

SELECT
    *
FROM 
    working_hours ;

