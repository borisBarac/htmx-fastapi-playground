from pydantic import BaseModel, field_validator

from .validators import mac_address_validate

class UserTemplateData(BaseModel):
  epoch_time: int
  mac_address: str
  template_state: dict | None = None
  template_base64: str | None = None

  @field_validator('mac_address')
  @classmethod
  def mac_validate(cls, mac_address: str) -> str:
    return mac_address_validate(mac_address)

  class Config:
    json_schema_extra = {
      "example": {
        "epoch_time": "732873827837",
        "mac_address": "98:43:FA:28:3C:14"
      }
    }

if __name__ == "__main__":
    pass