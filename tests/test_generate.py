from datetime import datetime

from parsy import generate, regex, string


@generate
def parser():
    year = yield regex(r"\d{4}").map(int)
    month = yield string("/") >> regex(r"\d{2}").map(int)
    day = yield string("/") >> regex(r"\d{2}").map(int)
    return datetime(year, month, day)


def test_generate():
    assert parser.parse("2024/02/10") == datetime(2024, 2, 10)
