#!/usr/bin/python
# All ways to run rostful and all Manager commands
# should be defined here for consistency
from __future__ import absolute_import
import os
import sys
import click

#importing current package if needed ( solving relative package import from __main__ problem )
if __package__ is None:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from celeros import celeros_worker
else:
    from . import celeros_worker

import logging
from logging.handlers import RotatingFileHandler


@click.command()
@click.option('-b', '--broker-url', default='redis://localhost:6379')  # by default use config module value
@click.option('-t', '--worker-tasks', default='celeros.tasks')  # by default use config module value
@click.option('-r', '--ros_args', default='')
def work(broker_url='', worker_tasks='', ros_args=''):

    logging.info('boker %r tasks %r', broker_url, worker_tasks)
    logging.info('ros_args %r', ros_args)

    #TODO : when called from python and no master found, do as roslaunch : create a master so it still can work from python
    #Launch the server
    celeros_worker.launch(broker_url, worker_tasks, ros_args.split())

if __name__ == '__main__':
    work()
