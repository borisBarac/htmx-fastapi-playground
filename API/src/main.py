import base64
import json
from operator import contains
from typing import Any

from fastapi import FastAPI, HTTPException, Query, Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from jinja2 import Template
from pydantic import ValidationError

from .model import UserTemplateData

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def value_error_template(request: Request) -> HTMLResponse:
  return templates.TemplateResponse(
    request=request, name="Input_err.html", status_code=422
  )


@app.exception_handler(Exception)
async def handle_error(request: Request, exc: Exception) -> HTMLResponse:
  # if you get more then 1 custom exception move this to ERROR middleware
  if isinstance(exc, (ValueError, ValidationError, RequestValidationError)):
    return value_error_template(request)

  raise HTTPException(
    status_code=500,
    detail="Internal Server Error, something went wrong!)",
  )


@app.get("/", response_class=HTMLResponse)
async def root_example(request: Request) -> HTMLResponse:
  return templates.TemplateResponse(request=request, name="index.html", status_code=200)


"""
Test data
html encoded: ICA8IURPQ1RZUEUgaHRtbD4KICA8aHRtbD4KICA8aGVhZD4KICAgIDx0aXRsZT5XZWxjb21lITwvdGl0bGU+CiAgPC9oZWFkPgogIDxib2R5PgogICAgPGgxPkhlbGxvLCB7eyBuYW1lIH19ITwvaDE+CiAgICA8cD5XZWxjb21lIHRvIG91ciB3ZWJzaXRlLjwvcD4KICA8L2JvZHk+CiAgPC9odG1sPg==
state for html {"name": "bob"}
"""


def render_preview_data(request: Request, data: UserTemplateData) -> Response:
  if data.template_base64 is None or data.template_state is None:
    raise ValueError("Did not get any template data")

  context: dict = data.template_state
  # JS and PYTHON BEATY
  template_str: str = data.template_base64.replace(" ", "+")
  bytes = base64.b64decode(template_str)
  template_str = bytes.decode()

  # Render the template with the context
  rendered_output = Template(template_str).render(context)
  return Response(content=rendered_output, status_code=200, media_type="text/html")


@app.post("/render", response_class=HTMLResponse)
async def base64_renderer(request: Request, data: UserTemplateData) -> Response:
  return render_preview_data(request, data)


@app.get("/render")
async def get_user(
  request: Request,
  epoch_time: int = Query(..., description="epoch time of the req"),
  session_id: str = Query(..., description="mac address of the device"),
  template_state_base64: str | None = Query(
    None, description="render template state in base64"
  ),
  template_html_base64: str | None = Query(None, description="html template in base64"),
) -> Response:
  if template_state_base64 is None or template_html_base64 is None:
    raise ValueError("Template data is not provided")

  t_state_bytes = base64.b64decode(template_state_base64)

  template_state_dict: dict[str, Any] = json.loads(t_state_bytes)
  user_template_data = UserTemplateData(
    epoch_time=epoch_time,
    session_id=session_id,
    template_state=template_state_dict,
    template_base64=template_html_base64,
  )

  return render_preview_data(request, user_template_data)
