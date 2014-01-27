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
import webapp2
import logging

def handle_404(request, response, exception):
    logging.exception(exception)
    response.write('Oops! I could swear this page was here!')
    response.set_status(404)

def handle_500(request, response, exception):
    logging.exception(exception)
    response.write('A server error occurred!')
    response.set_status(500)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class NonMainHandler(webapp2.RequestHandler):
    def get(self):
        foo = self.app.config.get('foo')
        self.response.write('Hello %s!!' % foo)

class FormMainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('''<form action="/form" method="post">
                               <input name="input" type="text" />
		               <input value="submit" type="submit" />
                               </form>''')
    def post(self):
        input = self.request.get('input')
        self.response.write("<html><body><p>%s</p></body></html>"
                                    % (input))

routes = [ ('/', MainHandler),
           ('/test', NonMainHandler),
           ('/form', FormMainHandler)
         ]

config = {'foo': 'bar'}


app = webapp2.WSGIApplication(routes=routes, debug=True, config=config)

app.error_handlers[404] = handle_404
app.error_handlers[500] = handle_500
