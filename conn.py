import redis
import pymysql

REDIS = redis.Redis(host='127.0.0.1', port=6379)
def mysql_connect():
  return pymysql.connect(host='127.0.0.1', user='root', password='', db='bot', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)