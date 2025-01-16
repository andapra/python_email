#!/usr/bin/env python

"""Tests for `python_email` package."""

import pytest


from src.python_email.python_email import emailNotifications


@pytest.fixture
def test_email_parameters():
    return emailNotifications(from_email="alexanderdan.pratama94@gmail.com",
                              to_email=["adpratama@esriindonesia.co.id"],
                              password="wlmq exck gner aksz",
                              subject="TEST PYTHON EMAIL",
                            #   message="Hello World"
                              )

def test_send_email_tls(test_email_parameters):
    test_email_parameters.send_email_smtp_tls("Hello using tls")
    assert test_email_parameters.status_code == 200 

def test_send_email_ssl(test_email_parameters):
    test_email_parameters.send_email_smtp_ssl("Hello using ssl")
    assert test_email_parameters.status_code == 200