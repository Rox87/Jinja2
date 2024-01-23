from WrapperFunction.main import app
from WrapperFunction.myjinja import origem
from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_api_route("/csv", origem.from_csv.my_csv, methods=["GET"])
app.add_api_route("/json", origem.from_json.my_json, methods=["GET"])
app.add_api_route("/pandas", origem.from_pandas.my_pandas, methods=["GET"])
app.add_api_route("/sqlite", origem.from_sqlite.my_sqlite, methods=["GET"])