"""For hashes, the hash-max-ziplist-entries directive sets the total no. of fields
   that can be encoded to 512. The hash-max-ziplist-value directive sets the max size
   the hash is converted from a ziplist with a default size of 64.

    In this test we will test the size difference b/w ziplist and the linked-list for hashes.

    Note: Chaning the thrashold value of sets, hashes and lists with ziplist on an existing
    database won't chnage the pre-exisitng values. It will only encode the new data onwards.
"""
import uuid

from redis_conn import redis_conn


def ziplist_hahses(runs: int=500, size: int=512) -> int:
    """This we will call twice with different size
    and objserve the memory uses.

    Args:
        runs (int): Total fields we want to store
        size (int): max no of fields we want to set for ziplist

    Example:
    In [2]: print(zp.ziplist_hahses(size=512))
    Out[2]: 3102

    In [3]: print(zp.ziplist_hahses(size=0))
    Out[3]: 3764

    """
    key = f'test-hash:{size}'

    redis_ins = redis_conn._get_redis_connection()
    
    redis_ins.config_set('hash-max-ziplist-entries', size)

    run, zip_list, linked_list = [], [], []

    for i in range(runs):
        field = f'f{i}'
        redis_ins.hset(key, field, i)
        debug = redis_ins.debug_object(key)
        zip_list.append(debug.get('serializedlength'))

    return redis_ins.debug_object(key).get('serializedlength')


def ziplist_lists(runs=1000, size=512):
    """This we will call twice with different size
    and objserve the memory uses.

    Args:
        runs (int): Total fields we want to store
        size (int): max no of fields we want to set for ziplist

    Example:
    In [2]: print(zp.ziplist_lists(size=512))
    Out[2]: 15756

    In [3]: print(zp.ziplist_lists(size=0))
    Out[3]: 18946

    """
    key = f'test-list:{size}'

    redis_ins = redis_conn._get_redis_connection()
    
    redis_ins.config_set('list-max-ziplist-entries', size)

    run, zip_list, linked_list = [], [], []

    for i in range(runs):
        run.append(i)
        uid = uuid.uuid4()
        redis_ins.lpush(key, uid)
        debug = redis_ins.debug_object(key)
        zip_list.append(debug.get('serializedlength'))

    return redis_ins.debug_object(key).get('serializedlength')
