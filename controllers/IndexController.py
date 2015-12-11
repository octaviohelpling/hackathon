class IndexController(webapp2.RequestHandler):
    def get(self):
    	name = self.request.params.get('name')
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.out.write(template.render(name=name))
