import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'hello-world-server.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'database-west'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or '[SQL_USER_NAME_GOES_HERE]'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or '[SQL_PASSWORD_GOES_HERE]'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'helloworld123456'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'h22ikQe9nS4hQ786TcRvSAe7jkTQSeSomSTUQsxxS8Bg55i51vxaOpkzg+LmvtutF1qnEYddLTkL+AStGq9c6A=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
