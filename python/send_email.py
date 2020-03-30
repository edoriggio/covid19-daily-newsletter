# Copyright  2020  Edoardo Riggio
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

import os
import json
import smtplib
# Modules for sending an email
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

key = ''

script_dir = os.path.dirname('covid-19_daily_newsletter')
rel_path = 'secret.json'
passw = os.path.join(script_dir, rel_path)

with open(passw, 'r') as file:
    data = json.load(file)
    key = data['sendinblue']

def send_email(recipient, body, images, world_flag = ''):
    """
    Send an email using sendinblue's smpt relay

    Args:
        recipient (str): The email address of the subscriber
        body (str): The custom HTML body of the email
        images (list): A list containing all paths of the
                       generated graphs
    """

    strFrom = 'officialercapps@gmail.com'
    strTo = recipient

    msg = MIMEMultipart('alternative')
    msg['From'] = strFrom
    msg['To'] = strTo
    msg['Subject'] = 'Your Daily COVID-19 Summary'

    msgText = MIMEText(body, 'html')
    msg.attach(msgText)

    for n, i in enumerate(images):
        with open(i, 'rb') as file:
            msgImage = MIMEImage(file.read())
            msgImage.add_header('Content-ID', '<image{}>'.format(n))
            msg.attach(msgImage)

    if world_flag != '':
        with open(world_flag, 'rb') as file:
            msgImage = MIMEImage(file.read())
            msgImage.add_header('Content-ID', '<world_flag>'.format(n))
            msg.attach(msgImage)

    s = smtplib.SMTP('smtp-relay.sendinblue.com', 587)
    s.starttls()
    s.login("officialercapps@gmail.com", key)
    s.sendmail(strFrom, strTo, msg.as_string())
    s.quit()
    