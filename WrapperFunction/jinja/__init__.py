from WrapperFunction.myapp import app
from WrapperFunction.jinja import routes
from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_api_route("/data/csv", routes.csv_data.my_csv, methods=["GET"])
app.add_api_route("/data/json", routes.json_data.my_json, methods=["GET"])
app.add_api_route("/data/pandas", routes.pandas_data.my_pandas, methods=["GET"])
app.add_api_route("/data/sqlite", routes.sqlite_data.my_sqlite, methods=["GET"])