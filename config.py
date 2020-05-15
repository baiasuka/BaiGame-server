DIALECT = 'mysql'
DRIVER = 'pymysql'
DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_USERNAME = 'root'
DB_PASSWORD = 'ang318ang'
DATABASE = 'BaiGame'
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4".format(DIALECT, DRIVER, DB_USERNAME, DB_PASSWORD, DB_HOST,
                                                                      DB_PORT, DATABASE)
# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存，如果不必要的可以禁用它。
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 设置是否在每次连接结束后自动提交数据库中的变动。
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
# 指定数据库连接池的超时时间。默认是 10。
SQLALCHEMY_POOL_TIMEOUT = 20
# 自动回收连接的秒数。这对MySQL是必须的，默认情况下MySQL会自动移除闲置8小时或者以上的连接,Flask-SQLAlchemy会自动地设置这个值为 2 小时。也就是说如果连接池中有连接2个小时被闲置，那么其会被断开和抛弃；
SQLALCHEMY_POOL_RECYCLE = 1200
# 数据库连接池的大小。默认是数据库引擎的默认值 （通常是 5）。
SQLALCHEMY_POOL_SIZE = 10
# 控制在连接池达到最大值后可以创建的连接数。当这些额外的连接使用后回收到连接池后将会被断开和抛弃。保证连接池只有设置的大小；
SQLALCHEMY_MAX_OVERFLOW = 16


REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_CACHE_DB = 1
REDIS_PASSWORD = "ang318"
REDIS_CACHE_DB_EXPIRED = 3600