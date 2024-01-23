from jinja2 import Environment, FileSystemLoader
from fastapi.responses import HTMLResponse
import csv
async def my_csv():
    '''jinja2 loading a csv file'''
    # Crie um ambiente Jinja2 e especifique o diretório dos templates
    env = Environment(loader=FileSystemLoader('.'))

    # Carregue o template do arquivo
    template = env.get_template(f'templates/cities_csv.html')

    # Defina variáveis para o template
    var_file= "data/cities_sample.csv"
    with open(var_file) as f:
        data = csv.DictReader(f)

        # Renderize o template com as variáveis fornecidas
        html_content = template.render(data=data).encode('utf-8')

    return HTMLResponse(content=html_content, status_code=200)
