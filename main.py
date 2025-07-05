from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from models import User
import json
from pathlib import Path

app = FastAPI()
templates = Jinja2Templates(directory="templates")

DATA_FILE = Path("data/received_data.json")
DATA_FILE.parent.mkdir(exist_ok=True)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Hello Nexmedis! My name is Evangelista, 24 years old."}

# Kirim JSON
@app.get("/send-data", response_model=User)
def send_data():
    return {"name": "Evangelista", "age": 24}

# Terima JSON (POST)
@app.post("/receive-data")
def receive_data(user: User):
    data = user.dict()
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)
    return {"message": "Data received successfully", "data": data}

# Webpage menampilkan dan mengedit data
@app.get("/page", response_class=HTMLResponse)
def view_page(request: Request):
    data = {"name": "", "age": ""}
    if DATA_FILE.exists() and DATA_FILE.stat().st_size > 0:
        with open(DATA_FILE) as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                pass  # tetap pakai data default kosong
    return templates.TemplateResponse("index.html", {"request": request, "data": data})

# Endpoint untuk terima form dari webpage
@app.post("/submit-form")
def submit_form(name: str = Form(...), age: int = Form(...)):
    user = User(name=name, age=age)
    with open(DATA_FILE, "w") as f:
        json.dump(user.dict(), f)
    return RedirectResponse("/page", status_code=303)