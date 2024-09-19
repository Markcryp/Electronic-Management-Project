import click
from models import Electronic, Feature
from config import init_db

@click.group()
def cli():
    """Electronic Management CLI"""
    pass

@cli.command()
def init():
    """Initialize the database"""
    init_db()
    click.echo("Database initialized.")

@cli.command()
def add_electronic():
    """Add a new electronic item"""
    name = click.prompt("Enter name")
    brand = click.prompt("Enter brand")
    price = click.prompt("Enter price", type=float)
    Electronic.add_electronic(name, brand, price)
    click.echo(f"Electronic '{name}' added.")

@cli.command()
def list_electronics():
    """List all electronics and their features"""
    electronics = Electronic.list_electronics()
    if electronics:
        for electronic in electronics:
            click.echo(f"{electronic.id}: {electronic.name} ({electronic.brand}) - ${electronic.price}")
            features = Feature.get_features(electronic.id)
            if features:
                click.echo("  Features:")
                for feature in features:
                    click.echo(f"    - {feature.feature_name}")
            else:
                click.echo("  No features available.")
    else:
        click.echo("No electronics found.")

@cli.command()
def add_feature():
    """Add a feature to an electronic item"""
    electronic_id = click.prompt("Enter the electronic ID", type=int)
    feature_name = click.prompt("Enter feature name")
    Feature.add_feature(electronic_id, feature_name)
    click.echo(f"Feature '{feature_name}' added to electronic ID {electronic_id}")

@cli.command()
def delete_electronic():
    """Delete an electronic item"""
    electronic_id = click.prompt("Enter the electronic ID", type=int)
    Electronic.delete_electronic(electronic_id)
    click.echo(f"Electronic item with ID {electronic_id} deleted.")

@cli.command()
def update_electronic():
    """Update an electronic item"""
    electronic_id = click.prompt("Enter the electronic ID", type=int)
    name = click.prompt("Enter new name")
    brand = click.prompt("Enter new brand")
    price = click.prompt("Enter new price", type=float)
    Electronic.update_electronic(electronic_id, name, brand, price)
    click.echo(f"Electronic item with ID {electronic_id} updated.")

if __name__ == "__main__":
    cli()
