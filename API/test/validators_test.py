import unittest

from src.validators import session_id_validate, html_validate


class TestMACAddressValidation(unittest.TestCase):
  def test_valid_mac_address(self) -> None:
    result = session_id_validate("2313213weweweweqeqweqw22weqw")
    self.assertEqual(result, "2313213weweweweqeqweqw22weqw")

  def test_invalid_mac_address(self) -> None:
    self.assertRaises(ValueError, lambda: session_id_validate("dasdsadsadsaUIUIUIUIUIUIUI"))

  def test_html_validate(self) -> None:
    v_str = "<!doctypehtml><title>Simple Page</title><h1>Hello, world!</h1>"
    e_str = "<!doctypehtml><title>Simple Page</title><h1>Hello, world!"

    self.assertTrue(len(html_validate(v_str)) > 0)
    self.assertTrue(len(html_validate(e_str)) > 0)


if __name__ == "__main__":
  unittest.main()
