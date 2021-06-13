"""Here we will look into how we can save a lot of memory by just using
bitmap instead of a set.
"""
import random

from redis_conn import redis_conn


def populate(redis_set: bool=True):
    """ We will populate two differnt keys with same value
    but using different data structure.

    Note: Poulate the set first with below command
    127.0.0.1:6379> sadd ded/atom ded:1 ded:4
    (integer) 2

    Example:
        In [2]: sp.populate()
        Out[2]: 53766

        In [3]: sp.populate(redis_set=False)
        Out[3]: 1252

        Total keys in both set and bitmap
        127.0.0.1:6379> scard ded/atom
        (integer) 6048
        127.0.0.1:6379> bitcount ded/atomed
        (integer) 6034

        Here i missed creating the same rows, but we can do this by populate
        data in both set and bitmap in a single function call only.

    """
    redis_ins = redis_conn._get_redis_connection()
    for i in range(10000):
        if random.random() <= 0.6:
            member = i
            key = 'ded/atomed'
            if redis_set:
                member = f'ded/{i}'
                key = 'ded/atom'
                redis_ins.sadd(key, member)
            else:
                redis_ins.setbit(key, i, 1)
    
    return redis_ins.debug_object(key).get('serializedlength')
