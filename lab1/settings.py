from pydantic_settings import BaseSettings, SettingsConfigDict
from config import Job

class MainSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    DO_JOB: Job = Job.TO_STAR




class RpcSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    TO_STAR_URL: str = 'http://to-star:8000/api/v1/do'
    TO_SLASH_URL: str = 'http://to-slash:8000/api/v1/do'