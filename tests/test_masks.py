import unittest

from src.masks import get_mask_account, get_mask_card_number


class TestMasks(unittest.TestCase):
    def test_get_mask_card_number(self) -> None:
        self.assertEqual(
            get_mask_card_number("1234 1234 1234 1234"),
            "1234 ** **** 1234",
        )
        self.assertEqual(
            get_mask_card_number("1234"),
            "Номер карты должен содержать 16 цифр. Попробуйте ещё раз.",
        )
        self.assertEqual(
            get_mask_card_number("abcd"),
            "Формат номера карты неверный, он должен состоять только из цифр.",
        )

    def test_get_mask_account(self) -> None:
        self.assertEqual(get_mask_account("12345678901234567890"), "*****7890")
        self.assertEqual(
            get_mask_account("12345"),
            "Номер счета должен содержать 20 цифр. Попробуйте ещё раз.",
        )
        self.assertEqual(
            get_mask_account("abcde"),
            "Формат номера счета неверный, он должен состоять только из цифр.",
        )


if __name__ == "__main__":
    unittest.main()
