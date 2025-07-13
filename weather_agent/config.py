
import os

import yaml


class Config:
    def __init__(self, config_filename: str):
        self.CONFIG = {}
        self._read_config_yaml(config_filename)

    def _read_config_yaml(self, filename: str):
        config_path = os.path.join(os.path.dirname(__file__), filename)

        try:
            with open(config_path, 'r') as file:
                self.CONFIG = yaml.safe_load(file)
        except yaml.YAMLError as e:
            print(f"Warning: Error parsing YAML file '{config_path}': {e}")
        except FileNotFoundError:
            print(f"Error parsing YAML file '{config_path}' not found.")

    def get(self, *keys: tuple[str], default=None):
        value = self.CONFIG
        try:
            for key in keys:
                value = value[key]
            return value
        except (KeyError, TypeError):
            return default
