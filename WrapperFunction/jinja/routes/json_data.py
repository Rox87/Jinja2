from jinja2 import Environment, FileSystemLoader
from fastapi.responses import HTMLResponse
import json
async def my_json():
    '''Jinja2 from a json file'''
    # Crie um ambiente Jinja2 e especifique o diretório dos templates
    # Step 1: Read Parquet file using Pandas
    with open('data/cities_sample.json', 'r') as f:
        data = json.loads(f.read())

    # Step 2: Load Jinja2 environment and template
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('templates/cities_json.html')

    # Step 3: Render the template with the data
    html_content = template.render(data=data)

    # Step 4: Print or save the rendered content
    return HTMLResponse(content=html_content, status_code=200)
