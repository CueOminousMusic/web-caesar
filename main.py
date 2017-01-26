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
import caesar

class MainHandler(webapp2.RequestHandler):
    def get(self):
        message = ""
        encrypted_message = caesar.encrypt(message, 13)

        message_label = "<label>Type a message:</label>"
        textarea = "<textarea name='message'>" + encrypted_message + "</textarea>"

        rot_label = "<label>Rotate by:</label>"
        rot_input = "<input type='number' name='rotation'?>"

        submit = "<input type='submit'/>"
        form = ("<form method = 'post'>" +
                message_label + textarea + "<br>" +
                rot_label + rot_input + "<br>" +
                submit + "</form>")

        self.response.write(form)
        #self.response.write('Hello world!')

    def post(self):
        message = self.request.get("message")
        rotation = int(self.request.get("rotation"))
        encrypted_message = caesar.encrypt(message, rotation)
        encrypted_response = "Secret Message: " + encrypted_message
        self.response.write(encrypted_response)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
