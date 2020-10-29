# -*- coding: utf-8 -*-
"""Initialization of the project"""

from {{cookiecutter.package_name}}._logging import configure_logging
from {{cookiecutter.package_name}}.settings import Development
from {{cookiecutter.package_name}}.settings import init_project_settings

SETTINGS = init_project_settings()


logger = configure_logging(
   '{{cookiecutter.package_name}}', SETTINGS, kidnap_loggers=True
)
