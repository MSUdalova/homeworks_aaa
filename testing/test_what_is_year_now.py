import urllib.request
import json
from io import StringIO
from unittest.mock import patch
import pytest

API_URL = 'http://worldclockapi.com/api/json/utc/now'

YMD_SEP = '-'
YMD_SEP_INDEX = 4
YMD_YEAR_SLICE = slice(None, YMD_SEP_INDEX)

DMY_SEP = '.'
DMY_SEP_INDEX = 5
DMY_YEAR_SLICE = slice(DMY_SEP_INDEX + 1, DMY_SEP_INDEX + 5)


def what_is_year_now() -> int:
    """
    Получает текущее время из API-worldclock и извлекает из поля 'currentDateTime' год
    Предположим, что currentDateTime может быть в двух форматах:
      * YYYY-MM-DD - 2019-03-01
      * DD.MM.YYYY - 01.03.2019
    """
    with urllib.request.urlopen(API_URL) as resp:
        resp_json = json.load(resp)
        print(resp_json)

    datetime_str = resp_json['currentDateTime']
    if datetime_str[YMD_SEP_INDEX] == YMD_SEP:
        year_str = datetime_str[YMD_YEAR_SLICE]
    elif datetime_str[DMY_SEP_INDEX] == DMY_SEP:
        year_str = datetime_str[DMY_YEAR_SLICE]
    else:
        raise ValueError('Invalid format')

    return int(year_str)


def test_correct_date_ymd():
    exp_resp = '{"currentDateTime": "2021-12-06T13:06Z"}'
    with patch('urllib.request.urlopen', return_value=StringIO(exp_resp)):
        real_year = what_is_year_now()
        exp = 2021
    assert real_year == exp


def test_correct_date_dmy():
    exp_resp = '{"currentDateTime": "02.12.2021T13:52Z"}'
    with patch('urllib.request.urlopen', return_value=StringIO(exp_resp)):
        real_year = what_is_year_now()
        exp = 2021
    assert real_year == exp


def test_incorrect_date_sep():
    exp_resp = '{"currentDateTime": "2021_12_06T13:06Z"}'
    with patch('urllib.request.urlopen', return_value=StringIO(exp_resp)):
        with pytest.raises(ValueError):
            what_is_year_now()


def test_incorrect_resp_key():
    exp_resp = {'currentDate': '2021-12-06T13:06Z'}
    with patch('urllib.request.urlopen', return_value=exp_resp):
        with pytest.raises(AttributeError):
            what_is_year_now()


def test_incorrect_date_value():
    exp_resp = '{"currentDateTime": "2021.12.6T13:06Z"}'
    with patch('urllib.request.urlopen', return_value=StringIO(exp_resp)):
        with pytest.raises(ValueError):
            what_is_year_now()
