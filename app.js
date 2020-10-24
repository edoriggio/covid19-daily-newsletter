// Copyright  2020  Edoardo Riggio
// 
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
// 
//     http://www.apache.org/licenses/LICENSE-2.0
// 
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

require('dotenv').config()
const h = require('./website/scripts/hash_md5.js')

const express = require('express');
const request = require('request');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();

const MAILCHIMP_DC = process.env.MAILCHIMP_DC;
const MAILCHIMP_API_KEY = process.env.MAILCHIMP_API_KEY;
const MAILCHIMP_LIST_ID = process.env.MAILCHIMP_LIST_ID;

// Bodyparser Middleware
app.use(bodyParser.urlencoded({ extended: true }));

// Static folder
app.use(express.static(path.join(__dirname, 'website')));

// Signup Route for Mailchimp API call
app.post('/signup', (req, res) => {
  const { email, to_pass } = req.body;
  if (!email || !to_pass) {
    console.log('Please do not leave anything blank');
    return;
  } else if (!email.includes('@')) {
    console.log('Mail format is invalid');
    return;
  }

  // Construct req data
  const data = {
    members: [
        {
            email_address: email,
            status: 'subscribed',
            merge_fields: {
                COUNTRY: to_pass,
            }
        }
    ]
  };

  const postData = JSON.stringify(data);

  const options = {
    url: `https://${MAILCHIMP_DC}.api.mailchimp.com/3.0/lists/${MAILCHIMP_LIST_ID}`,
    method: 'POST',
    headers: {
      Authorization: `auth ${MAILCHIMP_API_KEY}`
    },
    body: postData
  };

  request(options, (err, response, body) => {
    if (err) {
      console.log(err, body)
      res.redirect('fail.html');
    } else {
      if (response.statusCode === 200) {
        res.redirect('success.html');
      } else {
        res.redirect('fail.html');
      }
    }
  });
});

//Unsubscribe Route for Mailchimp API call
app.post('/unsubscribe', (req, res) => {

  const { email, to_pass } = req.body;

  if (!email) {
    console.log('Please do not leave email blank');
    return;
  } else if (!email.includes('@')) {
    console.log('Mail format is invalid');
    return;
  }

  hash = h.hash_md5(email)

  const options = {
    url: `https://${MAILCHIMP_DC}.api.mailchimp.com/3.0/lists/${MAILCHIMP_LIST_ID}/members/${hash}/actions/delete-permanent`,
    method: 'POST',
    headers: {
      Authorization: `auth ${MAILCHIMP_API_KEY}`
    }
  };

  request(options, (err, response, body) => {
    if (err) {
      console.log(err, body)
      res.redirect('fail.html');
    } else {
      if (response.statusCode === 200) {
        res.redirect('success.html');
      } else {
        res.redirect('fail.html');
      }
    }
  });
});

const PORT = process.env.PORT || 5000;

app.listen(PORT, console.log(`Server started on ${PORT}`));
