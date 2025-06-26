import json
from pathlib import Path

import pandas as pd
import pytest

from src.reading_csv_xlsx_files import reading_file_csv, reading_file_xlsx

path_t = Path.cwd()


@pytest.fixture
def read_csv_new():
    path_csv = Path.cwd()
    file_path = path_csv / "transactions.csv"
    absolute_path = file_path.resolve()
    df = pd.read_csv(absolute_path, sep=";")
    js_dict = df.to_dict(orient="records")
    return json.dumps(js_dict, ensure_ascii=False, indent=4)


def test_read_csv(read_csv_new):
    expected_result = read_csv_new
    assert reading_file_csv(path_t) == expected_result


@pytest.fixture
def read_xlsx_new():
    path_csv = Path.cwd()
    file_path = path_csv / "transactions_excel.xlsx"
    absolute_path = file_path.resolve()
    df = pd.read_excel(absolute_path)
    js_dict = df.to_dict(orient="records")
    return json.dumps(js_dict, ensure_ascii=False, indent=4)


def test_read_xlsx(read_xlsx_new):
    expected_result = read_xlsx_new
    assert reading_file_xlsx(path_t) == expected_result
