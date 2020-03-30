![CDN Logo][logo]

## Inspiration

In a period as delicate as the one we are living in right now, being able to have the correct information is of fundamental importance. This is why we decided to create this project. We want to bring data and information to the user, not make him look through the whole internet, just to find that tiny piece of information he needs to know.

## What it does

Users can subscribe to the newsletter trough a webpage. Here they are requested to input their email address and by clicking on the next field, an overlay appears prompting them to choose which country to receive data and news of. The countries selected can be more the one, and there is also the possibility to choose "World" - to receive data and news about Covid-19 from around the world.

Once the user has completed the signup process, his job is done. Every day, at around 6pm, an email will be sent automatically to his inbox. The email will contain data regarding the spread of Covid-19 in the selected country with the aid of graphs, and link to the most recent news articles (which we plan to implement in the near future).

## Technologies used

For this project we used a variety of different technologies as well as some open source software.

- To create the logo and the design of the project we used **Figma**

- For the website we used **Node.js** to share the data given by the user input

- To manage the members list (sort of the backend part of this project) we used **Mailchimp's API**

- For the automatic mail creation and sent we used **Python 3.8**

- For the data we used [<u>**sagarkarira's coronavirus tracker CLI**</u>][github_link_1]

- For the generation of the graphs we used [<u>**Plotly**</u>][link_2]

- For the email SMTP server we used [<u>**Sendinblue**</u>][link_3]

## Challenges we ran into

Making this project was more difficult than we planned. The major issues we encountered when developing it were:

- Trying to connect the project to Mailchimp's API to send and request members lists (mainly in the website part of the project)

- Generating custom HTML code based on the users' country choices

- Find an easy and fast solution to were to save the members list (which we fortunately found in Mailchimp)

[logo]: ./branding/logo-extended.png
[github_link_1]: https://github.com/sagarkarira/coronavirus-tracker-cli
[link_2]: https://plotly.com/
[link_3]: https://www.sendinblue.com/
