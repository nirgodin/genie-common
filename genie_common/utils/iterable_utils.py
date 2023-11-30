from typing import Union, List, Iterator
from itertools import chain


def chain_lists(list_of_lists: Union[List[list], Iterator[list]]) -> list:
    return list(chain.from_iterable(list_of_lists))
