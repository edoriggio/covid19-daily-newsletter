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

import smtplib
# Modules for sending an email
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def send_email(reciever, body, images, world_flag = ''):
    """
    Send an email using sendinblue's smpt relay

    Args:
        reciever (str): The email address of the subscriber
        body (str): The custom HTML body of the email
        images (list): A list containing all paths of the
                       generated graphs
    """

    strFrom = 'officialercapps@gmail.com'
    strTo = reciever

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Your Daily COVID-19 Update'
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo

    msgAlternative = MIMEMultipart('alternative')
    msgAlternative['Subject'] = 'Your Daily COVID-19 Update'
    msgAlternative['From'] = strFrom
    msgAlternative['To'] = strTo
    msgRoot.attach(msgAlternative)

    msgText = MIMEText('Your Daily COVID-19 Update')
    msgAlternative.attach(msgText)

    msgText = MIMEText(body, 'html')
    msgAlternative.attach(msgText)

    for n, i in enumerate(images):
        with open(i, 'rb') as file:
            msgImage = MIMEImage(file.read())
            msgImage.add_header('Content-ID', '<image{}>'.format(n))
            msgRoot.attach(msgImage)

    if world_flag != '':
        with open(world_flag, 'rb') as file:
            msgImage = MIMEImage(file.read())
            msgImage.add_header('Content-ID', '<world_flag>'.format(n))
            msgRoot.attach(msgImage)

    s = smtplib.SMTP('smtp-relay.sendinblue.com', 587)
    s.starttls()
    # TODO: insert credentials
    s.login()
    message = "Message_you_need_to_send"
    s.sendmail(strFrom, strTo, message)
    s.quit()
    