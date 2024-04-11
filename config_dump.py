import tomli
import tomli_w
import glob
from os import mkdir
from os.path import dirname

def read_config():
    config = dict()
    for f in glob.glob("api/data/config/**/**.toml", recursive=True):
        config_name = f.removeprefix("api/data/config/").removesuffix(".toml")
        print(config_name)
        config[config_name] = dict()
        with open(f, 'rb') as fp:
            config[config_name] = tomli.load(fp)
    print(config)

def write_config():
    config = {'logger': {'general': {'level': 'debug', 'format': '%(asctime)s [%(levelname)s-%(filename)s] %(message)s'}, 'console': {'colorize': False, 'enabled': True}, 'filesystem': {'enabled': True, 'path': 'logs'}}, 'application': {'general': {'domain': 'localhost'}, 'api': {'debug': False, 'version': 'v1', 'prefix': '/api', 'cookie_secret': 'a', 'port': 58008}, 'task': {'database': 0, 'queue_name': 'queue1'}, 'archive': {'supported_extensions': 'zip'}}, 'database/redis': {'connection': {'host': 'redis', 'port': '6379'}}, 'database/arangodb': {'connection': {'protocol': 'http', 'host': 'arangodb', 'port': '8529', 'verify': 'false', 'database': 'db'}, 'root_credentials': {'username': 'root', 'password': 'rootpassword'}, 'user_credentials': {'username': 'user', 'password': 'user'}}, 'security/blacklist': {'database': {'memory_database': 1}}, 'security/anti_brute_force': {'general': {'active': False}, 'database': {'memory_database': 3}}, 'security/session': {'database': {'memory_database': 2}}, 'security/token': {'hasher': {'time_cost': 1, 'memory_cost': 1024, 'parallelism': 1, 'hash_length': 32, 'salt_length': 16}, 'jwt_token': {'access_expiration_time': 100000, 'refresh_expiration_time': 100000, 'access_secret_key': 'a', 'refresh_secret_key': 'a', 'algorithm': 'HS256'}}}
    for k in config.keys():
        f = f"api/data/config2/{k}.toml"
        try:
            mkdir(dirname(f))
        except FileExistsError:
            pass
        with open(f, 'wb') as fp:
            tomli_w.dump(config[k], fp)

write_config()
