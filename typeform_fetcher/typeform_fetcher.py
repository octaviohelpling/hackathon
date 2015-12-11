import json
import datetime
import time as tm
import uuid
from sqlalchemy import *
import json

details = {}
details['username'] = 'mahti'
details['password'] = 'Finlandia'

engine = create_engine('postgresql://' + details['username'] + ':' + details['password'] +'@10.15.0.1/helpling')

con = engine.connect()
max_time = con.execute("select max(updated_at) from requests")
con.close()

for rows in max_time:
    max_time_ = rows[0]
    
if max_time_ != None:
    timeint = int(tm.mktime(max_time_.utctimetuple()))

from urllib.request import Request, urlopen, URLError

# Get the data via api
if max_time_ == None:
    request = Request('https://api.typeform.com/v0/form/b8XMNw?key=26577e481bf84527924306074a7050b0b2c9bcbb&completed=true')
else: 
    request = Request('https://api.typeform.com/v0/form/b8XMNw?key=26577e481bf84527924306074a7050b0b2c9bcbb&completed=true&since=' +str(timeint))


try:
    response = urlopen(request)
    requests_raw = response.read()
except URLError:
    print('No kittez. Got an error code:')

    
requests_dict = json.loads(requests_raw.decode("utf-8"))

# Insert it into a database

metadata = MetaData(engine)

requests = Table('requests', metadata, autoload=True, autoload_with=engine)
    
i = requests.insert()

for responder in requests_dict['responses']:
    responder['answers']['updated_at'] = datetime.datetime.now()
    responder['answers']['request_id'] = uuid.uuid4()
    i.execute( responder['answers'] )    