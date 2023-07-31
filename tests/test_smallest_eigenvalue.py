from cvx.cli.smallest_eigenvalue import smallest_ev


def test_smallest_eigenvalue(resource_dir):
    file = resource_dir / "test.bson"

    smallest_ev(file)

