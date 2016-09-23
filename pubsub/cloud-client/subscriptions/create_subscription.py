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

# [START pubsub_create_subscription]
def create_subscription(topic_name, subscription_name):
    # References an existing topic, e.g. "my-topic"
    topic = pubsub_client.topic(topic_name)

    # Prepares a subscription instance, e.g. "my-new-subscription"
    subscription = topic.subscription(subscription_name)

    # Creates the subscription
    subscription.create()

    print('Created subscription: {}'.format(subscription.name))
# [END pubsub_create_subscription]
