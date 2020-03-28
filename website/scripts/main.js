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

let countries = ["afghanistan", "albania", "algeria", "andorra", "angola", "anguilla", "antigua-and-barbuda", "argentina", "armenia", "aruba", "australia", "austria", "azerbaijan", "bahamas", "bahrain", "bangladesh", "barbados", "belarus", "belgium", "belize", "benin", "bermuda", "bhutan", "bolivia", "bosnia", "brazil", "british-virgin-islands", "brunei", "bulgaria", "burkina-faso", "cabo-verde", "cambodia", "cameroon", "canada", "cayman-islands", "central-african-republic", "chad", "chile", "china", "coast-d-ivoire", "colombia", "congo", "costa-rica", "croatia", "cuba", "curacao", "czechia", "denmark", "djibouti", "dominica", "dominican-republic", "ecuador", "egypt", "el-salvador", "equatorial-guinea", "eritrea", "estonia", "ethiopia", "fiji", "finland", "france", "french-polynesia", "gabon", "gambia", "georgia", "germany", "ghana", "gibraltar", "greece", "greenland", "grenada", "guatemala", "guinea", "guinea-bissau", "haiti", "vatican-city", "honduras", "hong-kong", "hungary", "iceland", "india", "indonesia", "iran", "iraq", "ireland", "isle-of-man", "israel", "italy", "jamaica", "japan", "jordan", "kazakhstan", "kenya", "kwait", "kyrgyzstan", "laos", "latvia", "lebanon", "liberia", "libya", "liechtenstein", "lithuania", "luxembourg", "macao", "macedonia", "madagascar", "malasya", "maldives", "mali", "malta", "martinique", "mauritania", "mauritius", "mexico", "moldova", "monaco", "mongolia", "montenegro", "montserrat", "morocco", "mozambique", "myanmar", "namibia", "nepal", "netherlands", "new-zealand", "nicaragua", "niger", "nigeria", "norway", "oman", "pakistan", "palestine", "panama", "papua-new-guinea", "paraguay", "peru", "philippines", "poland", "portugal", "qatar", "romania", "russia", "rwanda", "south-korea", "saint-kitts-and-nevis", "st-lucia", "san-marino", "saudi-arabia", "senegal", "serbia", "seychelles", "singapore", "sint-maarten", "slovakia", "slovenia", "somalia", "south-africa", "spain", "sri-lanka", "sudan", "suriname", "swaziland", "sweden", "switzerland", "syria", "taiwan", "tanzania", "thailand", "togo", "trinidad-and-tobago", "tunisia", "turkey", "turks-and-caicos", "uae", "uk", "usa", "uganda", "ukraine", "uruguay", "uzbekistn", "venezuela", "vietnam", "zambia", "zimbabwe"];
let names = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Anguilla", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia", "Brazil", "British Virgin Islands", "Brunei", "Bulgaria", "Burkina Faso", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Cayman Islands", "Central African Republic", "Chad", "Chile", "China", "Coast D'Ivoire", "Colombia", "Congo", "Costa Rica", "Croatia", "Cuba", "Curacao", "Czechia", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Fiji", "Finland", "France", "French Polynesia", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Haiti", "Vatican City State", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Isle of Man", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macao", "Macedonia", "Madagascar", "Malaysia", "Maldives", "Mali", "Malta", "Martinique", "Mauritania", "Mauritius", "Mexico", "Moldova", "Monaco", "Mongolia", "Montenegro", "Montserrat", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Norway", "Oman", "Pakistan", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "South Korea", "Saint Kitts and Nevis", "Saint Lucia", "San Marino", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Singapore", "Sint Maarten", "Slovakia", "Slovenia", "Somalia", "South Africa", "Spain", "Sri Lanka", "Sudan", "Suriname", "Swaziland", "Sweden", "Switzerland", "Syriac", "Taiwan", "Tanzania", "Thailand", "Togo", "Trinidad and Tobago", "Tunisia", "Turkey", "Turks and Caicos", "UAE", "United Kingdom", "USA", "Uganda", "Ukraine", "Uruguay", "Uzbekistan", "Venezuela", "Vietnam", "Zambia", "Zimbabwe"];

var selected = [];
var countries_str_new = '';

//  Function that makes the overlay visible when a button is clicked
function unhide_overlay() {
    document.getElementById('overlay-back').style.visibility = 'visible';

    // Empty the array of selected elements
    if (selected.length != 0) {
        selected = [];
    }
}

// Function that hides the overlay when a button is clicked
function hide_overlay() { 
    document.getElementById('overlay-back').style.visibility = 'hidden';
}

// Function that creates custom <li> elements and appends them to the list-choices <ul>
function add_list_elements() { 
    for (i in countries) {
        var li = document.createElement('li');
        li.setAttribute('class', 'country');

        var img = document.createElement('img');
        var link = '../assets/flags/' + countries[i] + '.svg';
        img.setAttribute('class', 'flag');
        img.src = link;
        li.appendChild(img);

        var p = document.createElement('p');
        var text = names[i];
        p.setAttribute('class', 'country-name');
        p.innerHTML = text;
        li.appendChild(p);

        var checkFake = document.createElement('input');
        checkFake.setAttribute('id', names[i]);
        checkFake.setAttribute('class', 'check-fake')
        checkFake.type = 'checkbox';
        li.appendChild(checkFake);

        var check = document.createElement('span');
        check.setAttribute('class', 'check');
        li.appendChild(check);

        var divider = document.createElement('hr');
        divider.setAttribute('class', 'divider');
        li.appendChild(divider);

        document.getElementById('list-choices').appendChild(li);
    }
}

// Function that checks which countries have been checked by the user and changes
// placeholder <p> in order to display a summary of the chosen countries
function check_which_checked() {
    var countries_str = ''

    for (i in names) {
        if (document.getElementById(names[i]).checked) {
            selected.push(names[i])
        }
    }

    for (i in selected) {
        if (i < selected.length - 1) {
            countries_str_new += selected[i] + ', ';
        } else {
            countries_str_new += selected[i];
        }
    }
    
    // Check the length of the array so that only a few country names
    // are visible (to avoid cluttering)
    if (selected.length == 2) {
        countries_str = selected[0] + ' and ' + selected[1];
        document.getElementById('placeholder').style.color = '#000000';
    } else if (selected.length == 1) {
        countries_str = selected[0];
        document.getElementById('placeholder').style.color = '#000000';
    } else if (selected.length == 0) {
        countries_str = 'Select countries'
        document.getElementById('placeholder').style.color = '#cdcdcd';
    } else {
        countries_str = selected.length + ' countries'
        document.getElementById('placeholder').style.color = '#000000';
    }
    
    document.getElementById('placeholder').innerHTML = countries_str;
}

// Function called when the option "world" is clicked. Here the World string
// is substituted with the placeholder and all elements in the <ul> are
// unchecked
function world_checked() {
    selected = ['World'];
    document.getElementById('placeholder').innerHTML = selected.toString();
    document.getElementById('placeholder').style.color = '#000000';

    // Uncheck all checked boxes
    for (i in names) {
        if (document.getElementById(names[i]).checked) {
            document.getElementById(names[i]).checked = false;
        }
    }

    hide_overlay();
}
