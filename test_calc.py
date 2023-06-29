import pytest

import calc


@pytest.mark.parametrize(
    ("x", "y", "expected"),
    [
        (-2, -3, -5),
        (0, -3, -3),
        (2, -3, -1),
        (-2, 0, -2),
        (-2, 3, 1),
        (0, 0, 0),
        (2, 3, 5),
    ],
)
def test_add_number(x: int | float, y: int | float, expected: int | float) -> None:
    assert calc.add_number(x, y) == expected
