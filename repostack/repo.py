# -*- coding: utf-8 -*-

import subprocess

from .utils import (
    mkdir,
    cd,
    rm,
    render_template,
)

import click


@click.command()
@click.option('--name', prompt='Repo name', help='project name')
@click.option('--template', prompt="Choose a template [Maven, Go]", type=click.Choice(['Maven', 'Go']))
def create_repo(name, template):
    repo_path = mkdir(name)
    repo_tpl = template.capitalize()
    try:
        with cd(repo_path):
            subprocess.check_call(['git', 'init'])

            for template in ('{}.gitlab-ci.yml.tpl',):
                render_template(template.format(repo_tpl), name, '.gitlab-ci.yml')

            for template in ('{}.pre-commit.tpl',):
                render_template(template.format(repo_tpl), name, folder='.git/hook')
    except Exception as e:
        rm(repo_path)
        raise e


cmds = [create_repo]
