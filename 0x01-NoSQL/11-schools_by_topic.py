#!/usr/bin/env python3
''' schools by topic'''


def schools_by_topic(mongo_collection, topic):
    ''' retuns list of schools with specific topics '''
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },

    }

    return [doc for doc in mongo_collection.find(topic_filter)]
