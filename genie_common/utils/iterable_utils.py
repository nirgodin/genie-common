from collections import Counter
from typing import Union, List, Iterator, Any
from itertools import chain


def chain_lists(list_of_lists: Union[List[list], Iterator[list]]) -> list:
    return list(chain.from_iterable(list_of_lists))


def find_most_common_element(lst: List[Any]) -> Any:
    counter = Counter(lst)
    most_common_main_genre = counter.most_common(1)
    element, count = most_common_main_genre[0]

    return element
