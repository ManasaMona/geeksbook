
import os
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))


class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class MainHandler(Handler):
    def get(self):
    	username = self.request.get("username")
        email = self.request.get("email")
        password = self.request.get("pwd")
        gender = self.request.get("gender")
    	self.render('index.html')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
