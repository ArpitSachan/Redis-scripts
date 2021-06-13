"""Here we will look into high-level and very memory-efficient techinique
   using Redis hashes.
"""

import pymarc

from redis_conn import redis_conn


def inject_data():
    """Get the MARC 21 record and store the data in our redis.

    Example:
    """

    marc_reader = pymarc.MARCReader(open('tutt-library-popular.mrc', 'rb'), to_unicode=True)
    for record in marc_reader:
        _basic_ingestion(record)


def _basic_ingestion(record):
    """Takes a marc record and converts it into JSON and save the
    result as string in Redis.

    Args:
        record (MARC21 reccord)

    """
    redis_ins = redis_conn._get_redis_connection()
    marc_json = record.as_json()
    redis_key = 'marc:{}'.format(redis_ins.incr('global:marc'))
    redis_ins.set(redis_key, marc_json)
