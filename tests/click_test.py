"""This makes the test creating database setup"""
# pylint: disable=redefined-outer-name, line-too-long
# import logging
import os

from click.testing import CliRunner

from app import create_database

runner = CliRunner()


def test_create_database():
    """This creates a database"""
    response = runner.invoke(create_database)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    dbdir = os.path.join(root, '../database')
    # make a directory if it doesn't exist
    assert os.path.exists(dbdir) is True
