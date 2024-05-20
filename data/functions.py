import csv
import os
import pickle
from tqdm import tqdm
from .types import (
    ALL_PREDICTOR_NAMES,
    PredictorName,
    SignedPredictorsEntry
)
from typing import Callable


__all__ = (
    "read_signed_predictors_results",
)


def _parse[T](value: str, type_converter: Callable[[str], T] = str) -> T:
    if value == "": raise ValueError("Value cannot be None")
    return type_converter(value)


def _parse_optional[T](value: str, type_converter: Callable[[str], T] = str) -> T | None:
    return None if value == "" else type_converter(value)


def _read_signed_predictors_results_from_original_file() -> tuple[SignedPredictorsEntry, ...]:
    all_values: list[SignedPredictorsEntry] = []
    with open(os.path.join(os.path.dirname(__file__), "signed_predictors_dl_wide.csv")) as f:
        reader = csv.reader(f)
        header = next(reader, None)
        assert header is not None
        assert len(header) == len(ALL_PREDICTOR_NAMES) + 2
        assert header[0] == "permno"
        assert header[1] == "yyyymm"
        for i in range(len(ALL_PREDICTOR_NAMES)):
            assert header[i+2] == ALL_PREDICTOR_NAMES[i]

        for row in tqdm(reader, total=5_156_870):
            assert len(row) == len(ALL_PREDICTOR_NAMES) + 2
            assert len(row[1]) == 6 and row[1].isdigit()
            sub_values: dict[PredictorName, float | None] = {}
            for i, predictor in enumerate(ALL_PREDICTOR_NAMES):
                sub_values[predictor] = _parse_optional(row[i+2], float)
            all_values.append({
                "permno": _parse(row[0], int),
                "yyyymm": row[1],
                **sub_values # type: ignore
            })

    return tuple(all_values)


def read_signed_predictors_results(*, fast_mode: bool = True) -> tuple[SignedPredictorsEntry, ...]:
    """Reads all the predictor results.

    If `fast_mode` is enabled, the reading of the file should be about 5.5 times faster.

    :param fast_mode: If `True`, reads the generated `.pkl` file, else reads the original `.csv` file. Defaults to `True`.
    :return: The tuple of all the predictor entry (each one being a typed dictionary).
    """
    if not fast_mode:
        return _read_signed_predictors_results_from_original_file()
    with open(os.path.join(os.path.dirname(__file__), "signed_predictors_results.pkl"), "rb") as f:
        return pickle.load(f)
