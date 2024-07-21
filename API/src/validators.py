import re
from lxml import etree


def session_id_validate(id: str) -> str:
  pattern = r".*[0-9].*[A-Za-z]"
  match = re.match(pattern, id)

  if len(id) > 10 and match:
    return id
  else:
    raise ValueError("Id does not meet the requirements")

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
