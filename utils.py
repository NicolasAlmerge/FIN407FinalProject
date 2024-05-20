import os
from typing import Literal


__all__ = (
    "get_data_file_path",
    "get_env",
)


def get_data_file_path(file_name: str, /) -> str:
    return os.path.join("data", file_name)


def get_env(key: Literal["WRDS_USERNAME"], /) -> str:
    with open(".env") as f:
        for line in f.read().split():
            line_key, line_value = line.split("=")
            if line_key.strip() == key:
                return line_value.strip()
    raise ValueError("Could not find requested key")
