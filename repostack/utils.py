import os
import sys
import shutil
import logging
import contextlib

from jinja2 import (
    Environment,
    FileSystemLoader
)


def jinja_load_env():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(current_dir, 'templates')
    return Environment(loader=FileSystemLoader(template_dir))


jinja_env = jinja_load_env()


def mkdir(path):
    if os.path.exists(path) and os.path.isdir(path):
        return

    try:
        os.mkdir(path)
        return os.path.join(os.getcwd(), path)
    except OSError:
        logging.error("create {} failed".format(path))
        sys.exit(1)


@contextlib.contextmanager
def cd(path):
    current_dir = os.getcwd()
    os.chdir(path)
    yield path
    os.chdir(current_dir)


def rm(path):
    if os.path.exists(path):
        shutil.rmtree(path)


def render_template(template_name, repo_name, file_name=None, folder='.'):
    if file_name is None:
        if not template_name.endswith('.tpl'):
            raise ValueError("Filename extension '.tpl' required")
        file_name = '.'.join(os.path.basename(template_name).split('.')[1:-1])

    path = os.path.join(folder, file_name)
    content = jinja_env.get_template(template_name).render(repo=repo_name)

    if os.path.exists(path):
        return

    mkdir(folder)
    with open(path, 'wb') as project_file:
        project_file.write(content.encode('utf8'))

    return path
