from fastapi import FastAPI, Body, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
app = FastAPI()

list_of_username = []
templates = Jinja2Templates(directory='templates')


class NameValue(BaseModel):
    name: str = None
    country: str
    age: int
    base_salary: float


@app.get("/home/{user_name}", response_class=HTMLResponse)
def write_home(request: Request, user_name: str):
    return templates.TemplateResponse('home.html', {"request": request, "username": user_name})


@app.post('/postData')
def post_data(namevalue: NameValue, spousal_status: str = Body(...)):
    print(NameValue)
    return {
        "name": namevalue.name,
        "spousal status": spousal_status
    }
