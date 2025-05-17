import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card():
    assert mask_account_card("Maestro 7000792289606361") == "Maestro 7000 79** **** 6361"
    assert mask_account_card("47700079228960636115") == "4770 **6115"


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("47700079228960636115", "4770 **6115"),
        ("", "Неверно введены данные"),
        ("hdkflbc", "Неверно введены данные"),
    ],
)
def test_mask_account_card_params(value, expected):
    assert mask_account_card(value) == expected


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2025.05.13") == "13.05.2025"
    assert get_date("") == "Введите дату"
