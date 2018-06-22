import os
import logging
from docx import Document
from docxcompose.composer import Composer
from datetime import datetime
from argparse import ArgumentParser

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def join_with_base_dir(path):
    if path.startswith('/'):
        return path
    else:
        return os.path.join(BASE_DIR, path)


def merge(input_dir):
    logger.info('Gather files..')

    files = os.listdir(input_dir)
    files = filter(lambda x: not x.startswith(('.', '~')) and x.endswith('.docx'), files)
    files = sorted([os.path.join(input_dir, file_) for file_ in files])

    logger.info('Merging files..')
    master = Document(files.pop(0))
    composer = Composer(master)
    for file_ in files:
        composer.append(Document(file_))

    return composer


def save(output_path, composer):
    if os.path.isdir(output_path):
        file_path = os.path.join(output_path, 'combined-%s.docx' % datetime.now().strftime('%Y-%m-%dT%H.%M.%S'))
    elif os.path.isdir(os.path.dirname(output_path)):
        file_path = os.path.join(os.path.dirname(output_path), os.path.basename(output_path))
    else:
        logger.fatal('Output directory does not exist: %s',
                     output_path if os.path.isdir(output_path) else os.path.dirname(output_path))
        return

    logger.info('Save generated docx: %s' % file_path)
    composer.save(file_path)


if __name__ == '__main__':
    parser = ArgumentParser(prog='Docxcompose Merger')
    parser.add_argument('-d', type=str, default='templates', nargs='?',
                        help='Folder with .docx files to merge. Files are sorted by name, like this the first one'
                             'will be the master file.')
    parser.add_argument('-o', type=str, default='export', nargs='?', help='Output directory or output filename')
    args = parser.parse_args()

    input_dir = join_with_base_dir(args.d)
    output_path = join_with_base_dir(args.o)

    composer = merge(input_dir)
    save(output_path, composer)



