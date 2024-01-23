from jinja2 import Environment, FileSystemLoader
from fastapi.responses import HTMLResponse
import sqlite3
async def my_sqlite():
    '''Jinja2 from a sqlite database'''
    # Crie um ambiente Jinja2 e especifique o diretório dos templates
    env = Environment(loader=FileSystemLoader('.'))

    # Carregue o template do arquivo
    template = env.get_template(f'templates/cities_sqlite.html')

    # Defina variáveis para o template
    var_file= "data/cities_sqlite3.db"

    connection = sqlite3.connect("data/cities_sqlite3.db")
    cursor = connection.cursor()

    data=[]
    for row in cursor.execute("SELECT * FROM cities"):
        data.append(row)

        # Renderize o template com as variáveis fornecidas
    html_content = template.render(data=data).encode('utf-8')

    return HTMLResponse(content=html_content, status_code=200)
