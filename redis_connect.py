#!/usr/bin/python
import redis

RedisPool = redis.ConnectionPool(host='localhost', port=6379, db=0)

def GetKey(key_name):
    RedisConn = redis.Redis(connection_pool=RedisPool)
    response = RedisConn.get(key_name)
    print response
    return 

def SetKey(key_name, key_value):
    RedisConn = redis.Redis(connection_pool=RedisPool)
    response = RedisConn.set(key_name, key_value)
    if response==True:
        print "Key Value added successfully"
    else:
        print "Invalid Operation"
    return



SetKey("jahantech","Redis is good!")


GetKey("jahantech")

GetKey("doesntexist")
