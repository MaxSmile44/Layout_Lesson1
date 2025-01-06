import argparse
import collections
import datetime
import os
from dotenv import load_dotenv
import pandas
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


DATE_ESTABLISHMENT = 1920


def get_age():
    winery_age = datetime.date.today().year - DATE_ESTABLISHMENT
    year_name = 'лет'
    if (winery_age // 10) % 10 != 1:
        if winery_age % 10 == 1:
            year_name = 'год'
        elif winery_age % 10 in (2, 3, 4):
            year_name = 'года'
    return f'{winery_age} {year_name}'

def get_wines_info():
    load_dotenv()
    path = os.getenv('FILE_PATH')

    parser = argparse.ArgumentParser(description='Print "python main.py -p {name of excel file with wine data}" '
                                                 'or print "python main.py" '
                                                 'if there is a file .env with the default file path')
    parser.add_argument('-p', '--path', default=path, help='Path to excel file')
    args = parser.parse_args()

    excel_wines_df = pandas.read_excel(io=args.path)
    excel_wines_df = excel_wines_df.fillna('')
    wines = excel_wines_df.to_dict(orient='records')

    wine_categories = collections.defaultdict(list)
    for wine in wines:
        wine_categories[wine['Категория']].append(wine)
    wine_categories = dict(wine_categories)
    return wine_categories

def update_page():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        winery_age=get_age(),
        wine_categories=get_wines_info()
    )
    return rendered_page

def main():
    rendered_page = update_page()
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
