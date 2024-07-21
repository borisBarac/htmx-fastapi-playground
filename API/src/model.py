from pydantic import BaseModel, field_validator

from .validators import session_id_validate


class UserTemplateData(BaseModel):
  epoch_time: int
  session_id: str
  template_state: dict | None = None
  template_base64: str | None = None

  @field_validator("session_id")
  @classmethod
  def session_validate(cls, session_id: str) -> str:
    return session_id_validate(session_id)

  class Config:
    json_schema_extra = {
      "example": {
        "epoch_time": "732873827837",
        "mac_address": "98:43:FA:28:3C:14",
      }
    }


if __name__ == "__main__":
  pass
