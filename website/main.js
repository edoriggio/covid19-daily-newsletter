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

function unhide_overlay() {
    document.getElementById('overlay-back').style.visibility = 'visible';
}

function hide_overlay() {
    document.getElementById('overlay-back').style.visibility = 'hidden';
}

function add_list_elements() {
    var ul = document.getElementById('list-choices');
    var li = document.createElement('li');
    li.setAttribute('class','country');
    li.innerHTML = 'ciao'
    ul.appendChild(li);
}