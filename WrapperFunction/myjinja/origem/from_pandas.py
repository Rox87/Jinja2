from jinja2 import Environment, FileSystemLoader
from fastapi.responses import HTMLResponse
import pandas as pd
async def my_pandas():
    '''Jinja2 loading a parquet file in pandas dataframe'''
    # Crie um ambiente Jinja2 e especifique o diretório dos templates
    # Step 1: Read Parquet file using Pandas
    df = pd.read_parquet('data/cities_sample.parquet')

    # Step 2: Load Jinja2 environment and template
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('templates/cities_dataframe.html')

    # Step 3: Render the template with the data
    html_content = template.render(data=df)

    # Step 4: Print or save the rendered content
    return HTMLResponse(content=html_content, status_code=200)
