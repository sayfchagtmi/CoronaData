import click
from corona import parser, save, DataInfo

@click.command()
@click.option('--fpath', default='',
                help='The file path (By default current directory)')
@click.option('--date', default=True, type=bool,
                help='Set it True to show the update date (By default True)')
def run(fpath,date):
    """
    Download the latest updated data about coronavirus pandemic by country (Total Cases, New Cases,
    Total Deaths, New Deaths, Total Recovered, Active Cases, Serious Critical, Total cases/ 1M pop,
    Deaths/ 1M pop, Total Tests, Tests/ 1M pop).
    Source: https://www.worldometers.info/coronavirus/
    """
    print('Fetching data...')
    parsed_page = parser.parse_page()
    data = save.save_data(parsed_page,str(fpath))
    print(f'Data saved to "{data.fpath}"')
    if date:
        print(f'Data was last updated: {data.update_date}')

