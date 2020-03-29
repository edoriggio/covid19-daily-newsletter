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
# All needed modules imported from ipython
from IPython.display import display, HTML

subscribers: {str: list} = {'edo': ['Italy', 'China']}

data_url = 'https://corona-stats.online/?format=json'
data = requests.get(data_url).json()

def generate_graphs(subs):
    for user, countries in subscribers.items():
        bodies = []

        for country in countries:
            graphs = []

            if country == 'World':
                pass
            else:
                for i, n in zip(data['data'], range(len(data['data']))):
                    if i['country'] == country:
                        country_data = data['data'][n]

                        active_cases_labels = ['Mild condition', 'Critical condition']
                        active_cases_values = [country_data['active'] - country_data['critical'], country_data['critical']]
                        
                        figure1 = go.Figure(data=[go.Pie(labels=active_cases_labels, values=active_cases_values, hole=.5)])
                        figure1.update_layout(
                            annotations=[dict(text=country_data['active'], x=0.5, y=0.53, font_size=18, showarrow=False),
                                        dict(text='Active cases', x=0.5, y=0.47, font_size=12, showarrow=False)])

                        total_cases_labels = ['Recovered', 'Deaths']
                        total_cases_values = [country_data['recovered'], country_data['deaths']]

                        figure2 = go.Figure(data=[go.Pie(labels=total_cases_labels, values=total_cases_values, hole=.5)])
                        figure2.update_layout(
                            annotations=[dict(text=country_data['cases'], x=0.5, y=0.53, font_size=18, showarrow=False),
                                        dict(text='Total cases', x=0.5, y=0.47, font_size=12, showarrow=False)])

                        graphs.append(figure1)
                        graphs.append(figure2)            

def save_graphs(graphs_list):
    for i, c in zip(graphs_list, range(len(graphs_list))):
        script_dir = os.path.dirname(__file__)
        rel_path = 'temp/figure_{}.png'.format(c)
        abs_file_path = os.path.join(script_dir, rel_path)
        i.write_image(abs_file_path)

def delete_temp_files():
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
