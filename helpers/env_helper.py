import os
from dotenv import load_dotenv


class EnvironmentHandler:
    """helps to get env vars using python-dotenv"""
    @staticmethod
    def get_env_variable(var_name):
        """get variables from env by name(var_name) """
        load_dotenv()
        return os.getenv(var_name)
