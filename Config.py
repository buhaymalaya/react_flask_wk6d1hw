import os
class Config:

  PROPAGATE_EXCEPTIONS = True
  API_TITLE = 'Film Club'
  API_VERSION = 'v1'
  OPENAPI_VERSION = '3.0.1'
  OPENAPI_URL_PREFIX = '/'
  OPENAPI_SWAGGER_UI_PATH = '/'
  OPENAPI_SWAGGER_UI_URL = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'
  SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URL')
  elephant_sql_api_key = os.environ.get('ELEPHANTSQL_API_KEY')