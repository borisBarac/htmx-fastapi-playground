import base64

from fastapi import FastAPI, Request, Response
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
  return templates.TemplateResponse(request=request,
                                    name="Input_err.html",
                                    status_code=422)

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError) -> HTMLResponse:
    return value_error_template(request)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
  return value_error_template(request)

@app.get("/", response_class=HTMLResponse)
async def root_example(request: Request) -> HTMLResponse:
  return templates.TemplateResponse(request=request,
                                    name="index.html",
                                    status_code=200)


'''
Test data
html encoded: ICA8IURPQ1RZUEUgaHRtbD4KICA8aHRtbD4KICA8aGVhZD4KICAgIDx0aXRsZT5XZWxjb21lITwvdGl0bGU+CiAgPC9oZWFkPgogIDxib2R5PgogICAgPGgxPkhlbGxvLCB7eyBuYW1lIH19ITwvaDE+CiAgICA8cD5XZWxjb21lIHRvIG91ciB3ZWJzaXRlLjwvcD4KICA8L2JvZHk+CiAgPC9odG1sPg==
state for html {"name": "bob"}
'''
@app.post("/render", response_class=HTMLResponse)
async def base64_renderer(request: Request, data: UserTemplateData) -> str:
  if data.template_base64 is None or data.template_state is None:
    raise ValueError('Did not get any template data')

  context: dict = data.template_state
  template_str: str = data.template_base64
  bytes = base64.b64decode(template_str)
  template_str = bytes.decode()

  # Render the template with the context
  rendered_output = Template(template_str).render(context)
  return Response(content=rendered_output,
                  status_code=200,
                  media_type="text/html")
