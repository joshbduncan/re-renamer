from pathlib import Path

import pytest

from re_renamer.app import REnamer


@pytest.fixture
def paths(tmp_path):
    paths = []
    for i in range(10):
        path = Path(tmp_path.joinpath(f"test_path_{i}.txt"))
        path.touch()
        paths.append(path)
    return paths


@pytest.fixture
def app(paths):
    return REnamer(paths)
