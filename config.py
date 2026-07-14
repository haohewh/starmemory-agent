"""星忆配置 - 通过环境变量或默认值设置"""
import os

class Settings:
    DB_PATH = os.environ.get("STARMEMORY_DB_PATH", "./starmemory.db")
    DEFAULT_MODEL = os.environ.get("STARMEMORY_MODEL", "gpt-4")
    
settings = Settings()
