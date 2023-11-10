import json

class ConfigManager:
    _instance = None

    

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        if ConfigManager._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self._load_config()

    def _load_config(self):
        # path
        conf_config_path = "conf/config.json"
        with open(conf_config_path, 'r') as f:
            self.config = json.load(f)

    @property
    def flyday_config(self):
        return self.config.get('flyday')

# 使用配置管理器
# config_manager = ConfigManager.get_instance()
# db_config = config_manager.database_config
# server_config = config_manager.server_config

# print(db_config)
# print(server_config)
