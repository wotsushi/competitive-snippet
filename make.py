import yaml
import json
import importlib
import os


if __name__ == "__main__":
    with open('langs.yml') as langs_yml:
        langs = yaml.load(langs_yml, Loader=yaml.FullLoader)
    for lang in langs:
        lang_name = lang['lang']
        ext = lang['ext']
        with open(f'{lang_name}/{lang_name}.yml') as snippet_srcs:
            snippet_list = yaml.load(snippet_srcs, Loader=yaml.FullLoader)
        parser = importlib.import_module(f'{lang_name}.parser').parse
        os.makedirs('json', exist_ok=True)
        with open(f'json/{lang_name}.json', 'w') as snippets_json:
            json.dump(
                {
                    snippet['name']: {
                        'prefix': snippet['prefix'],
                        'description': snippet['description'],
                        'body': parser(
                            f'{lang_name}/snippets/{group["package"]}/'
                            f'{snippet["name"]}.{ext}'
                        )
                    }
                    for group in snippet_list
                    for snippet in group['snippets']
                },
                snippets_json,
                indent=2
            )
