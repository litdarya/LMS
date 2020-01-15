# pylint: disable=no-value-for-parameter

import psycopg2
import click

connection = psycopg2.connect("dbname='lms_db' user='admin' host='localhost' password='admin'")


@click.command()
@click.option('--script', help='path to sql script to execute')
def create_tables(script):
    script = open(script).read()
    with connection.cursor() as cursor:
        print('executing')
        res = cursor.execute(script)
        print('res = ', res)
    connection.commit()
    print('committed')


if __name__ == "__main__":
    create_tables()