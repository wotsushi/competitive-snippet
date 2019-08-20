import click
import os
import yaml


@click.command()
def main():
    package_name = click.prompt('package name')
    snippet_name = click.prompt('snippet name')
    extention = click.prompt('extention', default='rs')
    prefix = click.prompt('prefix')
    description = click.prompt('description')

    snippet_dir = f'snippets/{package_name}/{snippet_name}'
    os.makedirs(snippet_dir, exist_ok=True)
    with open(f'{snippet_dir}/{snippet_name}.{extention}', 'w'):
        pass
    # TODO: Generaize
    with open('rust.yml', 'r') as snippet_yml:
        snippets = yaml.load(snippet_yml, Loader=yaml.FullLoader)
    package = next(
        (
            package
            for package in snippets
            if package['package'] == package_name
        ),
        None
    )
    if package:
        package['snippets'].append(
            {
                'name': snippet_name,
                'prefix': f'${prefix}',
                'description': description
            }
        )
    else:
        snippets.append(
            {
                'package': package_name,
                'snippets': [
                    {
                        'name': snippet_name,
                        'prefix': f'${prefix}',
                        'description': description
                    }
                ]
            }
        )
    with open('rust.yml', 'w') as snippet_yml:
        yaml.dump(snippets, snippet_yml, default_flow_style=False)


if __name__ == "__main__":
    main()
