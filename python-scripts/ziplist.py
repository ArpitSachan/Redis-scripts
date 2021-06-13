""" For hashes, list and sorted sets, this special encoding in based on ziplist A.
    The ziplist is specially coded doubly linked list which is designed to be very memory
    efficient. It stores both strings and integers. Where integers are encoded as an actual
    integers instead of memory inefficient a series of chars. It allows push and pop on both
    side in O(1) time.

    However, because every operation requires a reallocation of the memory used by the ziplist
    the actual complexity is related to the amount of memory used by ziplist.

    Depending  upon the size, type and contents of the data structures, the ziplist encoding
    offers significant memory savings for our redis database.

    Redis dynamically switches between the ziplist and the default encoding for the data 
    structure when the current limit for that Redis data type is reached.
"""


import redis
import settings


def run():
    redis_conn = _get_redis_connection()
    _dynamic_encoding_switch(redis_conn)


def _dynamic_encoding_switch(redis_conn):
    for i in range(515):
        redis_conn.hset('test-hash', i , 1)
        if  i > 510:
            debug = redis_conn.debug_object('test-hash')
            print('Count: {} Length: {} Encoding: {}'.format(i, debug.get('serializedlength'), debug.get('encoding')))


def _get_redis_connection():
    return redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
