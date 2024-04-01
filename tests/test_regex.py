import hypothesis.strategies as st
from hypothesis import given
from parsy import regex


@given(st.integers())
def test_regex(example: int):
    parser = regex(r"-?\d+").map(int)
    parser.parse(str(example)) == example
