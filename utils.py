import logging
import os
import pandas as pd
from rich.logging import RichHandler
from typing import Literal


__all__ = (
    "get_data_file_path",
    "get_env",
    "get_logger",
    "has_any_na",
    "read_from_parquet",
    "write_to_parquet",
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


def get_logger(name: str, minimum_level: int = logging.DEBUG) -> logging.Logger:
    """
    Gets a custom logger.

    :param name: Name of the logger.
    :param minimum_level: Minimum level of the logger.
    :return: Custom-made logger.
    """
    logging.basicConfig(format="%(message)s", datefmt="[%X]", handlers=[RichHandler()])
    logger = logging.getLogger(name)
    logger.setLevel(minimum_level)
    return logger


def has_any_na(df: pd.DataFrame, /) -> bool:
    return df.isna().any().any()


def read_from_parquet(file_name: str, /) -> pd.DataFrame:
    if not file_name.endswith(".parquet"):
        raise ValueError("File should end with '.parquet'")
    return pd.read_parquet(get_data_file_path(file_name), engine="pyarrow")


def write_to_parquet(df: pd.DataFrame, file_name: str, /, *, include_index: bool = False):
    if not file_name.endswith(".parquet"):
        raise ValueError("File should end with '.parquet'")
    df.to_parquet(get_data_file_path(file_name), engine="pyarrow", index=include_index)
