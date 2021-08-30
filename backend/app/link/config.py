from environs import Env

env = Env()

POSTGRES_USER = env.str('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = env.str('POSTGRES_PASSWORD', 'postgres')
POSTGRES_HOST = env.str('POSTGRES_HOST', 'db')
POSTGRES_PORT = env.str('POSTGRES_PORT', '5432')
POSTGRES_DB = env.str('POSTGRES_DB', 'shortener')

DB_URL = f'postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

