import base64
import json
from typing import Any
import unittest

from src.model import UserTemplateData


class TestUserStateModel(unittest.TestCase):
  def test_valid_model_no_template(self):
    s_id = "djhjhjkshakj2382KKKKK"
    result = UserTemplateData(epoch_time=123, session_id=s_id)
    self.assertIsInstance(result, UserTemplateData)
    self.assertEqual(result.epoch_time, 123)
    self.assertEqual(result.session_id, s_id)
    self.assertIsNone(result.template_state)

  def test_template_state_parsing(self):
    result = UserTemplateData(
      epoch_time=123,
      session_id="sjdkljskljd292829UYUIYI",
      template_state={"key1": "value", "key2": [1, 2, 3]},
    )

    template = result.template_state
    self.assertEqual(template["key1"], "value")
    self.assertEqual(template["key2"], [1, 2, 3])

  def test_invalid_model(self):
    with self.assertRaises(ValueError):
      UserTemplateData(epoch_time=123, mac_address="98:43:FA:28:3C:1X")

  def test_with_node_data(self):
    try:
      state64 = base64.b64decode(
        "ewogICAgImZOYW1lIjogIkpvaG4iLAogICAgImxOYW1lIjogIldpY2siLAogICAgIndlYXBvbnMiOiBbCiAgICAgICAgewogICAgICAgICAgICAia2V5IjogMSwKICAgICAgICAgICAgIm5hbWUiOiAiSGVja2xlciAmIEtvY2ggUDMwTCIsCiAgICAgICAgICAgICJhbW8iOiAxMgogICAgICAgIH0sIAogICAgICAgIHsKCiAgICAgICAgICAgICJrZXkiOiAxMiwKICAgICAgICAgICAgIm5hbWUiOiAiVFRJIEpXNCBQaXQgVmlwZXIiLAogICAgICAgICAgICAiYW1vIjogMTIKICAgICAgICB9LAogICAgICAgIHsKCiAgICAgICAgICAgICJrZXkiOiAyMSwKICAgICAgICAgICAgIm5hbWUiOiAiQ0EtNDE1L0hLNDE2IiwKICAgICAgICAgICAgImFtbyI6IDQ0CiAgICAgICAgfQogICAgXQp9"
      )
      template_state_dict: dict[str, Any] = json.loads(state64)
      result = UserTemplateData(
        epoch_time=1721596900,
        session_id="98:43:FA:28:3C:14",
        template_state=template_state_dict,
        template_base64="PCFET0NUWVBFIGh0bWw+CjxodG1sIGxhbmc9ImVuIj4KPGhlYWQ+CiAgPG1ldGEgY2hhcnNldD0iVVRGLTgiPgogIDxtZXRhIG5hbWU9InZpZXdwb3J0IiBjb250ZW50PSJ3aWR0aD1kZXZpY2Utd2lkdGgsIGluaXRpYWwtc2NhbGU9MS4wIj4KICA8dGl0bGU+TXkgU2ltcGxlIFdlYnNpdGU8L3RpdGxlPgo8L2hlYWQ+Cjxib2R5PgogIDxoMT5Nb3ZpZToge3tmTmFtZX19IHt7bE5hbWV9fTwvaDE+CiAgPGgyPldlYXBvbnMgPC9oMj4KICA8dWw+CiAgICB7JSBmb3IgaXRlbSBpbiB3ZWFwb25zICV9CiAgICAgICAgPGxpPnt7aXRlbS5uYW1lfX06IHt7aXRlbS5hbW99fTwvbGk+CiAgICB7JSBlbmRmb3IgJX0KICA8L3VsPgo8L2JvZHk+CjwvaHRtbD4g",
      )
      self.assertIsNotNone(result)
    except:  # noqa: E722
      self.fail()


if __name__ == "__main__":
  unittest.main()
