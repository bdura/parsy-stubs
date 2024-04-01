from datetime import datetime

from parsy import regex, seq, string

parser_combined = seq(
    regex(r"\d{4}").map(int),
    string("/") >> regex(r"\d{2}").map(int),
    string("/") >> regex(r"\d{2}").map(int),
).combine(datetime)

parser_combined_dict = seq(
    year=regex(r"\d{4}").map(int),
    month=string("/") >> regex(r"\d{2}").map(int),
    day=string("/") >> regex(r"\d{2}").map(int),
).combine_dict(datetime)


def test_generate():
    assert parser_combined.parse("2024/02/10") == datetime(2024, 2, 10)
    assert parser_combined_dict.parse("2024/02/10") == datetime(2024, 2, 10)
