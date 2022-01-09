import redis

IS_ATIVO_AMBIENTE_LOCAL=False


def get_connection_redis():
    if IS_ATIVO_AMBIENTE_LOCAL:
        return redis.Redis(host='localhost', port=6379)
    else:
        return redis.Redis(host='my_redis', port=6379)


class OcrCupomRedis:

    def __init__(self):
        self.connection = get_connection_redis()

    def get(self, key):
        response = self.connection.get(key)
        return response

    def save(self, key, value):
        self.connection.set(key, value, ex=20)