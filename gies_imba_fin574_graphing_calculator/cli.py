"""Console script for gies_imba_fin574_graphing_calculator."""
import sys
from xml.dom import ValidationErr
import click
import yaml
from .graphing_calculator import EquationsDefinition, draw_graph


@click.command()
@click.argument('curves_definition_file', type=click.File('r'))
def main(curves_definition_file):
    """Console script for gies_imba_fin574_graphing_calculator."""
    click.echo("Running Gies iMBA FIN574 Graphing Calculator...")
    click.echo("Loading curves definition...")

    curves_definition = yaml.safe_load(curves_definition_file)

    try:
        equations = EquationsDefinition.parse_obj(curves_definition)
        click.echo("Parsed demand equations:")
        for key, value in equations.demands.items():
            click.echo(f"{key}: {value}")

        click.echo("Parsed supply equations:")
        for key, value in equations.supplies.items():
            click.echo(f"{key}: {value}")

        draw_graph(equations)
    except ValidationErr as e:
        click.echo(f"Error parsing equations definition: {e}")
        sys.exit(1)



if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
