from fastapi import FastAPI, Path, Query, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import random, string, db

app = FastAPI()
templates = Jinja2Templates(directory='templates')  

# urls = {"abc" : "https://google.com/", "xyz" : "https://facebook.com/", "def" :"http://dinamalar.com/"}

#Getting input through form
@app.get("/", response_class=HTMLResponse)
def form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


    
#Converting to the shorten url
@app.post("/result")
def result(request: Request, url = Form(...)):
    print("Long url:", url)
    random_letters =''.join(random.choice(string.ascii_lowercase) for i in range(5))
    global urls
    short_url ="http://localhost:8000/"+ random_letters

    conn = db.get_connection()
    db.insert_url(conn, url, random_letters)
    conn.commit()
    conn.close()
    # urls[random_letters] = url
    return templates.TemplateResponse("result.html",  context = {"request": request, "url" :short_url})
    

#Redirect to the long url from short url 
@app.get("/{short_url}")
def redirect(short_url : str):
    # return RedirectResponse(url = urls[short_url])
    conn = db.get_connection()
    data = db.fetch_url(conn, short_url)
    print(data)
    conn.commit()
    conn.close()

    return RedirectResponse(data)
