#!/usr/bin/env python

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

import argparse
from subscriptions.create_subscription import create_subscription
from subscriptions.delete_subscription import delete_subscription
from subscriptions.list_subscriptions import list_subscriptions
from subscriptions.list_topic_subscriptions import list_topic_subscriptions
from topics.create_topic import create_topic
from topics.delete_topic import delete_topic
from topics.list_topics import list_topics


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    command_group_parser = parser.add_subparsers(dest='command_group')

    topics_command_parser = command_group_parser.add_parser('topics').add_subparsers(dest='command')

    topics_create_parser = topics_command_parser.add_parser('create', help=create_topic.__doc__)
    topics_create_parser.add_argument('topic_name')

    topics_delete_parser = topics_command_parser.add_parser('delete', help=delete_topic.__doc__)
    topics_delete_parser.add_argument('topic_name')

    topics_command_parser.add_parser('list', help=list_topics.__doc__)

    # publish_parser = subparsers.add_parser(
    #     'publish', help=publish_message.__doc__)
    # publish_parser.add_argument('topic_name')
    # publish_parser.add_argument('data')

    subscriptions_command_parser = command_group_parser.add_parser('subscriptions').add_subparsers(dest='command')

    subscriptions_create_parser = subscriptions_command_parser.add_parser('create', help=create_subscription.__doc__)
    subscriptions_create_parser.add_argument('topic_name')
    subscriptions_create_parser.add_argument('subscription_name')

    subscriptions_delete_parser = subscriptions_command_parser.add_parser('delete', help=delete_subscription.__doc__)
    subscriptions_delete_parser.add_argument('topic_name')
    subscriptions_delete_parser.add_argument('subscription_name')

    subscriptions_list_parser = subscriptions_command_parser.add_parser('list', help=list_subscriptions.__doc__)
    subscriptions_list_parser.add_argument('topic_name', nargs='?')

    args = parser.parse_args()

    if args.command_group == 'topics':
        if args.command == 'list':
            list_topics()
        elif args.command == 'create':
            create_topic(args.topic_name)
        elif args.command == 'delete':
            delete_topic(args.topic_name)
        # elif args.command == 'publish':
        #     publish_message(args.topic_name, args.data)
    elif args.command_group == 'subscriptions':
        if args.command == 'list':
            if args.topic_name:
                list_topic_subscriptions(args.topic_name)
            else:
                list_subscriptions()
        elif args.command == 'create':
            create_subscription(args.topic_name, args.subscription_name)
        elif args.command == 'delete':
            delete_subscription(args.topic_name, args.subscription_name)
