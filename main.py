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
import re

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)

def build_page(username_error, password_error, verify_error, email_error):
    user_label = "<label>Username</label>"
    user_input = "<input type='text' name='username'/>" + username_error

    pw_label = "<label>Password</label>"
    pw_input = "<input type='password' name='password'/>" + password_error

    ver_label = "<label>Verify Password</label>"
    ver_input = "<input type='password' name='verify'/>" + verify_error

    email_label = "<label>Email (optional)</label>"
    email_input = "<input type='email' name='email'/>" + email_error

    submit = "<input type='submit'/>"

    form = ("<form method='post'>" + user_label + user_input + "<br>" +
            pw_label + pw_input + "<br>" +
            ver_label + ver_input + "<br>" +
            email_label + email_input + "<br>" +
            submit + "</form>")

    return form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("", "", "", "")
        self.response.write(content)

    def post(self):
        error = False
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')


        if not valid_username(username):
            username_error = "That's not a valid username."
            error = True
        else:
            username_error = ""

        if not valid_password(password):
            password_error = "That's not a valid password."
            error = True
        else:
            password_error = ""

        if password != verify:
            verify_error = "Your passwords don't match."
            error = True
        else:
            verify_error = ""

        if not valid_email(email):
            email_error = "That's not a valid email."
            error = True
        else:
            email_error = ""

        content = build_page(username_error, password_error, verify_error, email_error)

        if error:
            self.response.write(content)
        else:
            self.redirect('/welcome?username=' + username)

class Welcome(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        self.response.write("Welcome, " + username + "!")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', Welcome)
], debug=True)
