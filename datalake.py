# Establish and define our database connections using SQLAlchemy:
import csv
import pathlib


def tree(directory):
    print(f'+ {directory}')

    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '    ' * depth
        print(f'{spacer}+ {path.name}')

data_dir = pathlib.Path(r'C:/Users/oxr0mqy/Projects/esbi_stream/data/')

print(tree(data_dir))
