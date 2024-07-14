import base64
import json

from fastapi import FastAPI, Query, Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from jinja2 import Template

from .model import UserTemplateData

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def value_error_template(request: Request) -> HTMLResponse:
  return templates.TemplateResponse(
    request=request, name="Input_err.html", status_code=422
  )


@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError) -> HTMLResponse:
  return value_error_template(request)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
  request: Request, exc: RequestValidationError
) -> HTMLResponse:
  return value_error_template(request)


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
  template_str: str = data.template_base64
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
  mac_address: str = Query(..., description="mac address of the device"),
  template_state_base64: str | None = Query(
    None, description="render template state in base64"
  ),
  template_html_base64: str | None = Query(None, description="html template in base64"),
) -> Response:
  try:
    t_state_bytes = base64.b64decode(template_state_base64)
    t_html_bytes = base64.b64decode(template_html_base64)

    template_state_dict: dict = json.loads(t_state_bytes)
    template_html_str: str = t_html_bytes.decode()
  except Exception as e:
    raise ValueError(e)

  return render_preview_data(
    request,
    UserTemplateData(epoch_time, mac_address, template_state_dict, template_html_str),
  )
