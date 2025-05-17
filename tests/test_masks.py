import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "value, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("7111792289606123", "7111 79** **** 6123"),
        ("7123792289606789", "7123 79** **** 6789"),
        ("1", "Некорректный номер карты"),
        ("70007922896063610000000", "Некорректный номер карты"),
        ("", "Некорректный номер карты"),
    ],
)
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("73654108430135874305", "**4305"),
        ("82654108430135871214", "**1214"),
        ("95644108430135875466", "**5466"),
        ("1", "Некорректный номер счета"),
        ("70007922896063610000000000000", "Некорректный номер счета"),
        ("", "Некорректный номер счета"),
    ],
)
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected


def test_get_mask_card_number_invalid_alpha():
    with pytest.raises(TypeError):
        assert get_mask_card_number("temnakdboe12sxgv")


def test_get_mask_account_invalid_alpha():
    with pytest.raises(TypeError):
        assert get_mask_account("oebfdvlirncadprsdl23")
