#! /usr/bin/env python
import pytest

PYTEST_ARGS = [
    '-s', '--cov=sebs', 'sebs/tests', '--cov-report', 'term-missing'
]

if __name__ == '__main__':
    pytest.main(PYTEST_ARGS)
