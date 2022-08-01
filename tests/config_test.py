"""This makes the test development setup"""
# pylint: disable=redefined-outer-name, line-too-long
# import logging
# import os

# import app.config


def test_development_config(application):
    """This makes development page"""
    application.config.from_object('app.config.DevelopmentConfig')

    assert application.config['DEBUG']
    assert not application.config['TESTING']


def test_testing_config(application):
    """This makes testing page"""
    application.config.from_object('app.config.TestingConfig')
    assert application.config['DEBUG']
    assert application.config['TESTING']
    assert not application.config['PRESERVE_CONTEXT_ON_EXCEPTION']
    # assert application.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///:memory:'


def test_production_config(application):
    """This makes production page"""
    application.config.from_object('app.config.ProductionConfig')
    assert not application.config['DEBUG']
    assert not application.config['TESTING']
