import unittest

from src.validators import mac_address_validate, html_validate


class TestMACAddressValidation(unittest.TestCase):
  def test_valid_mac_address(self) -> None:
    result = mac_address_validate("12:34:56:78:90:AB")
    self.assertEqual(result, "12:34:56:78:90:AB")

  def test_invalid_mac_address(self) -> None:
    self.assertRaises(ValueError, lambda: mac_address_validate("12:34:56:78:90:A"))

  def test_html_validate(self) -> None:
    v_str = "<!doctypehtml><title>Simple Page</title><h1>Hello, world!</h1>"
    e_str = "<!doctypehtml><title>Simple Page</title><h1>Hello, world!"

    self.assertTrue(len(html_validate(v_str)) > 0)
    self.assertTrue(len(html_validate(e_str)) > 0)


if __name__ == "__main__":
  unittest.main()
