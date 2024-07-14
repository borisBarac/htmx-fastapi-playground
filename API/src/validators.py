import re
from lxml import etree


def mac_address_validate(mac: str) -> str:
  """
  Validates the format of a MAC address string.

  Parameters:
      mac (str): The MAC address string to be validated.

  Returns:
      str: The validated MAC address string.

  Raises:
      ValueError: If the given string is not a valid MAC address.
  """
  pattern = r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})|([0-9a-fA-F]{4}\\.[0-9a-fA-F]{4}\\.[0-9a-fA-F]{4})$"
  if not re.match(pattern, mac):
    raise ValueError("given string is not a mac address")
  else:
    return mac


def html_validate(html_str: str) -> str:
  """
  Validates and fixes the HTML string without throwing exceptions.

  Parameters:
      html_str (str): The HTML string to be validated and fixed.

  Returns:
      str: The validated and fixed HTML string.
  """
  # validates and fixed, does not throw
  html_root = etree.HTML(html_str)
  return etree.tostring(html_root, encoding="unicode")


if __name__ == "__main__":
  pass
