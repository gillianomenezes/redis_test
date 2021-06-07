import redis
import json

redis_client = redis.Redis(host='localhost', port=6379, db=0)

data = {
    "name": "gilliano",
    "surname": "menezes"
}

resp = redis_client.get('mykey')

if resp:
    print('data fetched from redis')
    print(json.loads(resp))
else:
    print('data not available on redis. Setting it on')
    print(redis_client.set('mykey', json.dumps(data)))