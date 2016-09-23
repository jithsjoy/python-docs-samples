# Copyright 2016 Google Inc. All Rights Reserved.
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

from gcloud import pubsub
pubsub_client = pubsub.Client()

# [START pubsub_list_topics]
def list_topics():
    # Lists all topics in the current project
    topics = []
    next_page_token = None
    while True:
        page, next_page_token = pubsub_client.list_topics()
        topics.extend(page)
        if not next_page_token:
            break

    print('Topics:')
    for topic in topics:
        print(topic.name)
# [END pubsub_list_topics]
