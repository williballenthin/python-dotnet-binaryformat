import os.path

import pytest


@pytest.fixture
def dntojscript():
    # via: https://gist.github.com/caseysmithrc/b752447067b6f099f08baefe00978fad
    cd = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(cd, 'data', 'dntojscript.bin'), 'rb') as f:
        return f.read()
