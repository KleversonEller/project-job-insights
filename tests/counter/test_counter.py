from src.counter import count_ocurrences


def test_counter():
    count = count_ocurrences("src/jobs.csv", "javascript")

    assert count == 122
