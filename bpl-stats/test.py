from __init__ import *
import click

@click.command()
@click.option('--news', help='Current News')

def hello(news):
    apple = news()
    apple.news()

if __name__ == '__main__':
    hello()