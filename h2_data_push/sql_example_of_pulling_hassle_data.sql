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
select
*
from dwh_dl.busy_times
limit 10

-- AND

select
user_id,
start,
finish
from holidays

limit 100



-- The working hours of the providers

select
user_id,
day,
open_time,
close_time
from working_hours
where available
limit 1000
