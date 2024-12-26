import collections
import datetime
from pprint import pprint

import pandas
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

winery_age = datetime.date.today().year - datetime.date(year=1920, month=1, day=1).year
year_name='лет' if (str(winery_age)[-2:] in list(map(str, list(range(11, 21))))
                    or str(winery_age)[-1:] in list(map(str, list(range(5, 10))))
                    or str(winery_age)[-1:] == '0') \
    else 'года' if str(winery_age)[-1:] in list(map(str, list(range(2, 5)))) \
    else 'год'
excel_wines_df = pandas.read_excel(io='wine3.xlsx')
excel_wines_df = excel_wines_df.fillna('')
wines = excel_wines_df.to_dict(orient='records')

categories = excel_wines_df['Категория'].tolist()
wine_categories = collections.defaultdict(list)
for category in set(categories):
    for wine in wines:
        if category == wine['Категория']:
            wine_categories[category].append(wine)
wine_categories = dict(wine_categories)

rendered_page = template.render(
    winery_age=winery_age,
    year_name=year_name,
    wine_categories = wine_categories
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
