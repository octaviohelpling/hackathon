#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import webapp2
import jinja2
#import rest
from google.appengine.ext import ndb
#import MySQLdb

#from controllers import *
#from models import *

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)+'/Claas'),
    extensions=['jinja2.ext.autoescape'])

class IndexController(webapp2.RequestHandler):
    def get(self):
    	name = self.request.params.get('name')
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.out.write(template.render(name=name))

class MatchProviders(webapp2.RequestHandler):
	def getEvents(self):
#        db = MySQLdb.connect(unix_socket='/cloudsql/' + _INSTANCE_NAME, db='guestbook', user='root', charset='utf8')
		self.response.out.write('df')
		


ROUTES = [
	 ('/', IndexController)
	,('/match', MatchProviders)
]

app = webapp2.WSGIApplication(ROUTES, debug=True)
