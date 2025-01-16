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
                              message="Hello World")

def test_send_email_tls(test_email_parameters):
    assert test_email_parameters.send_email_smtp_tls()

def test_send_email(test_email_parameters):
    assert test_email_parameters.send_email_smtp_ssl()