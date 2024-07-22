# FastApi Jinja HTMX Template Playground

## What
> Playground for fast testing of Jinja templates with STATE injection in to them.
Templates are rendered in HTMX with FastAPI, so no local mock are used, the state is gonna go through the actual server. <br/>
[Jinja Docs](https://jinja.palletsprojects.com/en/3.1.x/) <br/>
[HTMX Docs](https://htmx.org)


## Features:
- Code editors with panel size chages
- Self reloading of data
- Code is persisted in a the local storage

## Install
- `docker compose up ./ `
- FE: `http://localhost:5173/`
- FastApi `http://localhost:8080/docs`

## Teck
- API: FastApi, Jinja templates, Htmx
- FE: Vue
- Deployments: Docker + Docker Compose