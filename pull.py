import click
import requests
import os
import shutil
import glob


ENDPOINT = 'https://judgedat.u-aizu.ac.jp'


@click.command()
@click.argument('snippet')
@click.argument('problem_id')
def main(snippet, problem_id):
    snippet_dir = next(iter(glob.glob(f'snippets/**/{snippet}')))
    in_dir = f'{snippet_dir}/in'
    shutil.rmtree(in_dir, ignore_errors=True)
    os.makedirs(in_dir)
    out_dir = f'{snippet_dir}/out'
    shutil.rmtree(out_dir, ignore_errors=True)
    os.makedirs(out_dir)

    res = requests.get(f'{ENDPOINT}/testcases/{problem_id}/header').json()
    serials = [header['serial'] for header in res['headers']]
    for serial in serials:
        testcase = requests.get(
            f'{ENDPOINT}/testcases/{problem_id}/{serial}').json()
        if (
            'terminated' not in testcase['in'] and
            'terminated' not in testcase['out']
        ):
            with open(f'{in_dir}/{serial:02}', 'w') as in_testcase:
                in_testcase.write(testcase['in'])
            with open(f'{out_dir}/{serial:02}', 'w') as out_testcase:
                out_testcase.write(testcase['out'])


if __name__ == "__main__":
    main()
