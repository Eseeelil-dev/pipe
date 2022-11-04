import os
import logging

import pytest

logger = logging.getLogger(__name__)


def cat_env():
    logger.info('\n'.join(map(lambda k: f'    {k} = {os.environ[k]}', os.environ)))


@pytest.mark.part1
def test_a_and_b():
    cat_env()
    a, b = 1, 1
    assert a == b, 'Unexpected result'


@pytest.mark.part2
def test_b_and_c():
    cat_env()
    b, c = 1, 1
    assert b == c, 'Unexpected result'
