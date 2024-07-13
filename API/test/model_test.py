import unittest

from src.model import UserTemplateData

class TestUserStateModel(unittest.TestCase):
  def test_valid_model_no_template(self):
    result = UserTemplateData(epoch_time=123, mac_address="98:43:FA:28:3C:14")
    self.assertIsInstance(result, UserTemplateData)
    self.assertEqual(result.epoch_time, 123)
    self.assertEqual(result.mac_address, "98:43:FA:28:3C:14")
    self.assertIsNone(result.template_state)

  def test_template_state_parsing(self):
    result = UserTemplateData(epoch_time=123,
                     mac_address="98:43:FA:28:3C:14",
                     template_state={"key1": "value",
                                     "key2": [1, 2, 3]
                                     })

    template = result.template_state
    self.assertEqual(template["key1"], "value")
    self.assertEqual(template["key2"], [1, 2, 3])

  def test_invalid_model(self):
    with self.assertRaises(ValueError):
      UserTemplateData(epoch_time=123, mac_address="98:43:FA:28:3C:1X")


if __name__ == '__main__':
    unittest.main()