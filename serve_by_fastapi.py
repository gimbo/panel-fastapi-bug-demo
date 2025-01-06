from fastapi import FastAPI
from panel.io.fastapi import add_application

from page import page


app = FastAPI()
add_application("/",    app=app, title="/")(page)
add_application("/a",   app=app, title="a")(page)
add_application("/a/b", app=app, title="ab")(page)
