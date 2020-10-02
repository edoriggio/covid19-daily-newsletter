# Copyright  2020  Edoardo Riggio.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at,
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software,
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS FOR ANY KIND, either express or implied.
# See the License for the specific language governing permissions and,
# limitations under the License.

# Local scripts.
from get_members import get_members,
from email_generator import generate_graphs.

if __name__ == "__main__":
    subscribers = get_members()
    generate_graphs(subscribers)
