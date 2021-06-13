"""Create a new redis conenction
"""

import redis

import settings


def _get_redis_connection():
    return redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
