from typing import Callable, List


def generate_list(start: int, stop: int, step: int = 1) -> List[int]:
    answer = []
    for i in range(start,stop,step):
        answer.append(i)
    return answer
    # """
    # Generate a list of integers.

    # :param start: Where to start the list (inclusive).
    # :param stop: Where to stop the list (exclusive).
    # :param step: How many digits apart each number is from the others around it.
    # :return: A list of integers.
    # """
    # pass  # implement me


def generate_list_with_strategy(start: int, stop: int, step: int, strategy: Callable) -> List[int]:
    answer = []
    for x in range(start, stop, step):
        answer.append(strategy(x))
    return answer
    # """
    # Generate a list of integers.

    # :param start: Where to start the list (inclusive).
    # :param stop: Where to stop the list (exclusive).
    # :param step: How many digits apart each number is from the others around it.
    # :param strategy: A function to manipulate each digit .
    # :return: A list of integers.
    # """
    # pass  # implement me
