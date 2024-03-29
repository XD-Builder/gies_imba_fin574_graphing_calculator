#!/usr/bin/env python

"""Tests for `gies_imba_fin574_graphing_calculator` package."""


import unittest
from click.testing import CliRunner

from gies_imba_fin574_graphing_calculator import graphing_calculator
from gies_imba_fin574_graphing_calculator import cli


class TestGies_imba_fin574_graphing_calculator(unittest.TestCase):
    """Tests for `gies_imba_fin574_graphing_calculator` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'gies_imba_fin574_graphing_calculator.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
