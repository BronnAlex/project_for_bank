import pytest
from src.widget import mask_account_card


def test_mask_account_card():
    assert mask_account_card("Maestro 7000792289606361") == "Maestro 7000 79** **** 6361"
    assert mask_account_card("47700079228960636115") == "4770 **6115"

@pytest.mark.parametrize("value, expected",
                         [
                             ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
                             ("47700079228960636115", "4770 **6115"),
                             ('', "Неверно введены данные"),
                             ("hdkflbc", "Неверно введены данные")
                         ])
def test_mask_account_card_params(value, expected):
    assert mask_account_card(value) == expected