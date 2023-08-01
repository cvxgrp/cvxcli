# -*- coding: utf-8 -*-
from typing import Dict

import fire  # type: ignore
import numpy as np

from cvx.bson.file import read_bson


def smallest_ev(bson_file) -> Dict[str, float]:
    """
    Compute the smallest eigenvalue of matrices stored in a bson file.

    There are faster methods to compute the smallest eigenvalue, e.g. an inverse power iteration.
    Here, we only use this as an example to work with the bson interface.

    On the command line

    poetry run smallest-eigenvalue cli/data/test.bson
    """

    eigenvalues = {
        key: np.min(np.linalg.eigh(matrix)[0])
        for key, matrix in read_bson(bson_file).items()
    }

    for key, ev in eigenvalues.items():
        print(key, ev)

    return eigenvalues


def main():  # pragma: no cover
    fire.Fire(smallest_ev)
