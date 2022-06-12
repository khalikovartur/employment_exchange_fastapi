from starlette.config import Config

config = Config('.env_dev')

DATABASE_URL = config('EE_DATABASE_URL', cast=str, default='')
ACCESS_TOKEN_EXPIRE_MIN = 60
ALGORITHM = 'HS256'
SECRET_KEY = config('EE_SECRET_KEY', cast=str,
    default='5c40873b099dc911e58fcadf44db847ce00c65ac98805c59fd4fb116f9cec064')