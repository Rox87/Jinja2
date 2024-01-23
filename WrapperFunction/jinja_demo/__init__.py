from WrapperFunction.myapp import app
from WrapperFunction.jinja.routers import api_routes
from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_api_route("/csv", api_routes.from_csv.my_csv, methods=["GET"])
app.add_api_route("/json", api_routes.from_json.my_json, methods=["GET"])
app.add_api_route("/pandas", api_routes.from_pandas.my_pandas, methods=["GET"])
app.add_api_route("/sqlite", api_routes.from_sqlite.my_sqlite, methods=["GET"])