ENVIRONMENT = "development"

C_APP_NAME = "socintel"

C_SECRET_KEY = "{}:PRODUCTION:Q1a!W2s@E3d#R4f$" \
               "".format(C_APP_NAME)

# Log Config
C_LOG_LEVEL = "DEBUG"
C_LOG_DIR = "log"

# SOC AUTH TOKEN
C_AUTH_CODE = ""
C_AUTH_TOKEN_LOCATION = "header"
C_HEADER_NAME = "ACCESS_TOKEN"
C_HEADER_TYPE = "Bearer"
C_AUTH_HEADER_CLIENT = 'Client'
C_AUTH_LOCAL_DISABLE = False

# SQLAlchemy config
C_PG_USER = C_APP_NAME
C_PG_PASS = ""
C_PG_HOST = "127.0.0.1"
C_PG_PORT = "5432"
C_PG_DB = C_APP_NAME

C_SOCEVENT_ADDRESS = "http://192.168.199.154:5007"
C_SOCEVENT_CODE = ""
C_SOCEVENT_CLIENT = "ssac"
C_SOCEVENT_RESULT_PULL_MAX_COUNT = 50
