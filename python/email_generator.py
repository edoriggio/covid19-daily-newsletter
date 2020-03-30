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
import shutil
import requests
# All needed modules imported from plotly
import chart_studio.plotly as plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots
# Local scripts
from get_members import get_members
from send_email import send_email

data_url = 'https://corona-stats.online/?format=json'
data = requests.get(data_url).json()

script_dir = os.path.dirname(__file__)

def generate_graphs(subs):
    """
    Given a dictionary of subscribers, email them the data summary

    Args:
        subs (dict): A dictionary containing the subscribers
    """
    for user, countries in subs.items():
        bodies = []
        images = []
        final_body = ''
        world_flag = False

        for numb, country in enumerate(countries):
            graphs = []
            email_body = ''

            if country == 'World':
                country_data = data['worldStats']
                world_flag = True

                # Create the graph for the active cases
                active_cases_labels = ['Mild condition', 'Critical condition']
                active_cases_values = [country_data['active'] - country_data['critical'], country_data['critical']]

                figure1 = go.Figure(data=[go.Pie(labels=active_cases_labels, values=active_cases_values, hole=.5)])
                figure1.update_layout(
                    annotations=[dict(text=country_data['active'], x=0.5, y=0.53, font_size=18, showarrow=False),
                                dict(text='Active cases', x=0.5, y=0.47, font_size=12, showarrow=False)])

                # Create the graph for the total cases
                total_cases_labels = ['Recovered', 'Deaths', 'Active']
                total_cases_values = [country_data['recovered'], country_data['deaths'], country_data['active']]

                figure2 = go.Figure(data=[go.Pie(labels=total_cases_labels, values=total_cases_values, hole=.5)])
                figure2.update_layout(
                    annotations=[dict(text=country_data['cases'], x=0.5, y=0.53, font_size=18, showarrow=False),
                                dict(text='Total cases', x=0.5, y=0.47, font_size=12, showarrow=False)])

                graphs.append(figure1)
                graphs.append(figure2)

                save_graphs(graphs, country.lower())

                template = (''
                    '<div style="width: 90%; left: 0; right: 0; margin: auto;">'
                        '<div style="padding-top: 10px">'
                            '<img src="cid:world_flag" style="height: 40px; vertical-align: middle;">'
                            '<p style="display: inline; padding-left: 18px; font-size: 20px; font-weight: bold;">{country}</p>'
                        '</div>'

                        '<div style="padding-top: 35px;">'
                            '<p style="display: inline; padding-left: 18px; font-size: 25px; font-weight: bold">Today</p>'

                            '<div style="padding-top: 10px;">'
                                '<div style="width: 100px; left: 0; right: 0; margin: auto;">'
                                    '<p style="line-height: 10px; font-size: 18px; font-weight: bold; text-align: center;">{new_cases}</p>'
                                    '<p style="line-height: 10px; font-size: 14px; text-align: center;">New Cases</p>'
                                '</div>'

                                '<div style="padding-top: 5px; width: 100px; left: 0; right: 0; margin: auto;">'
                                    '<p style="line-height: 10px; font-size: 18px; font-weight: bold; text-align: center;">{deaths}</p>'
                                    '<p style="line-height: 10px; font-size: 14px; text-align: center;">Deaths</p>'
                                '</div>'
                            '</div>'
                        '</div>'

                        '<div style="padding-top: 30px;">'
                            '<p style="display: inline; padding-left: 18px; font-size: 25px; font-weight: bold">Total</p>'

                            '<div style="padding-top: 10px;">'
                                '<img src="cid:image0">'
                                '<img src="cid:image1">'
                            '</div>'
                        '</div>'
                    '</div>'
                    '<hr>'
                '')

                images.append(os.path.join(script_dir, 'temp/figure_{}_0.png'.format(country.lower())))
                images.append(os.path.join(script_dir, 'temp/figure_{}_1.png'.format(country.lower())))

                _ = template
                _ = _.format(new_cases=country_data['todayCases'], deaths=country_data['todayDeaths'], country=country)
                email_body += _

                bodies.append(email_body)
            else:
                for i, n in zip(data['data'], range(len(data['data']))):
                    if i['country'] == country:
                        country_data = data['data'][n]

                        # Create the graph for the active cases
                        active_cases_labels = ['Mild condition', 'Critical condition']
                        active_cases_values = [country_data['active'] - country_data['critical'], country_data['critical']]

                        figure1 = go.Figure(data=[go.Pie(labels=active_cases_labels, values=active_cases_values, hole=.5)])
                        figure1.update_layout(
                            annotations=[dict(text=country_data['active'], x=0.5, y=0.53, font_size=18, showarrow=False),
                                        dict(text='Active cases', x=0.5, y=0.47, font_size=12, showarrow=False)])

                        # Create the graph for the total cases
                        total_cases_labels = ['Recovered', 'Deaths', 'Active']
                        total_cases_values = [country_data['recovered'], country_data['deaths'], country_data['active']]

                        figure2 = go.Figure(data=[go.Pie(labels=total_cases_labels, values=total_cases_values, hole=.5)])
                        figure2.update_layout(
                            annotations=[dict(text=country_data['cases'], x=0.5, y=0.53, font_size=18, showarrow=False),
                                        dict(text='Total cases', x=0.5, y=0.47, font_size=12, showarrow=False)])

                        graphs.append(figure1)
                        graphs.append(figure2)

                        save_graphs(graphs, country.lower())

                        template = (''
                            '<div style="width: 90%; left: 0; right: 0; margin: auto;">'
                                '<div style="padding-top: 10px">'
                                    '<img src="{flag}" style="height: 40px; vertical-align: middle;">'
                                    '<p style="display: inline; padding-left: 18px; font-size: 20px; font-weight: bold;">{country}</p>'
                                '</div>'

                                '<div style="padding-top: 35px;">'
                                    '<p style="display: inline; padding-left: 18px; font-size: 25px; font-weight: bold">Today</p>'

                                    '<div style="padding-top: 10px;">'
                                        '<div style="width: 100px; left: 0; right: 0; margin: auto;">'
                                            '<p style="line-height: 10px; font-size: 18px; font-weight: bold; text-align: center;">{new_cases}</p>'
                                            '<p style="line-height: 10px; font-size: 14px; text-align: center;">New Cases</p>'
                                        '</div>'

                                        '<div style="padding-top: 5px; width: 100px; left: 0; right: 0; margin: auto;">'
                                            '<p style="line-height: 10px; font-size: 18px; font-weight: bold; text-align: center;">{deaths}</p>'
                                            '<p style="line-height: 10px; font-size: 14px; text-align: center;">Deaths</p>'
                                        '</div>'
                                    '</div>'
                                '</div>'

                                '<div style="padding-top: 30px;">'
                                    '<p style="display: inline; padding-left: 18px; font-size: 25px; font-weight: bold">Total</p>'

                                    '<div style="padding-top: 10px;">'
                                        '<img src="cid:image{x}">'
                                        '<img src="cid:image{y}">'
                                    '</div>'
                                '</div>'
                            '</div>'
                            '<hr>'
                        '')

                        images.append(os.path.join(script_dir, 'temp/figure_{}_0.png'.format(country.lower())))
                        images.append(os.path.join(script_dir, 'temp/figure_{}_1.png'.format(country.lower())))

                        x = 0
                        y = 1
                        
                        if numb == 0:
                            x = 0
                            y = 1
                        else:
                            x = numb + 1
                            y = numb + 2

                        _ = template
                        _ = _.format(x=x, y=y , flag=country_data['countryInfo']['flag'], new_cases=country_data['todayCases'], deaths=country_data['todayDeaths'], country=country)
                        email_body += _

                        bodies.append(email_body)

        for i in bodies:
            final_body += i

        if world_flag:
            send_email(user, final_body, images, os.path.join(script_dir, 'world.png'))
        else:
            send_email(user, final_body, images)

    delete_temp_files()

def save_graphs(graphs_list, country):
    """
    Save the graphs in ./temp

    Args:
        graphs_list (list): A list of plotly graphs
        country (str): A string representing the current country
    """
    for i, c in zip(graphs_list, range(len(graphs_list))):
        script_dir = os.path.dirname(__file__)
        rel_path = 'temp/figure_{}_{}.png'.format(country, c)
        abs_file_path = os.path.join(script_dir, rel_path)
        i.write_image(abs_file_path)

def delete_temp_files():
    """
    Delete all files in ./temp
    """
    script_dir = os.path.dirname(__file__)
    rel_path = 'temp/'
    folder = os.path.join(script_dir, rel_path)
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
