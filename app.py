import click

from config import create_app


@click.group()
def cli():
    pass


@cli.command()
def dev():
    app = create_app('dev')
    app.run()


if __name__ == '__main__':
    cli()
