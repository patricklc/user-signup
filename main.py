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

def build_page():
    user_label = "<label>Username</label>"
    user_input = "<input type='text' name='user'/>"

    pw_label = "<label>Password</label>"
    pw_input = "<input type='password' name = 'pwd'/>"

    ver_label = "<label>Verify Password</label>"
    ver_input = "<input type='password' name = 'ver'/>"

    email_label = "<label>Email (optional)</label>"
    email_input = "<input type='email' name='usremail'/>"

    submit = "<input type='submit'/>"

    form = (user_label + user_input + "<br>" +
            pw_label + pw_input + "<br>" +
            ver_label + ver_input + "<br>" +
            email_label + email_input + "<br>" +
            submit)

    return form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page()
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
