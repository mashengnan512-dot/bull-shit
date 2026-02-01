import unittest

from duration_parser import parse_duration_seconds


class TestParseDurationSeconds(unittest.TestCase):
    def test_single_unit(self) -> None:
        self.assertEqual(parse_duration_seconds("45s"), 45)
        self.assertEqual(parse_duration_seconds("2m"), 120)
        self.assertEqual(parse_duration_seconds("3h"), 10800)
        self.assertEqual(parse_duration_seconds("1d"), 86400)

    def test_multiple_groups(self) -> None:
        self.assertEqual(parse_duration_seconds("1h30m"), 5400)
        self.assertEqual(parse_duration_seconds("2d 3h"), 2 * 86400 + 3 * 3600)

    def test_whitespace_between_number_and_unit(self) -> None:
        self.assertEqual(parse_duration_seconds(" 1 h  2 m 3 s "), 3600 + 120 + 3)

    def test_zero(self) -> None:
        self.assertEqual(parse_duration_seconds("0s"), 0)
        self.assertEqual(parse_duration_seconds("0h 0m 0s"), 0)

    def test_invalid(self) -> None:
        with self.assertRaises(ValueError):
            parse_duration_seconds("")
        with self.assertRaises(ValueError):
            parse_duration_seconds("   ")
        with self.assertRaises(ValueError):
            parse_duration_seconds("10")  # missing unit
        with self.assertRaises(ValueError):
            parse_duration_seconds("m")  # missing number
        with self.assertRaises(ValueError):
            parse_duration_seconds("1x")  # unknown unit
        with self.assertRaises(ValueError):
            parse_duration_seconds("-1s")  # not a digit
        with self.assertRaises(ValueError):
            parse_duration_seconds("1.5h")  # not an integer

    def test_type(self) -> None:
        with self.assertRaises(TypeError):
            parse_duration_seconds(None)  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()

