from math import ceil
from typing import Generator, Optional, Union, Any, List, Type

from genie_common.tools import AioPoolExecutor
from genie_common.typing import F, AF


class ChunksGenerator:
    def __init__(self, pool_executor: AioPoolExecutor, chunk_size: int, max_chunks_number: Optional[int] = None):
        self._pool_executor = pool_executor
        self._chunk_size = chunk_size
        self._max_chunks_number = max_chunks_number

    async def execute_by_chunk_in_parallel(self, lst: list, func: Union[F, AF], expected_type: Type[Any]) -> List[Any]:
        chunks = self.generate_data_chunks(lst=lst)
        return await self._pool_executor.run(
            iterable=list(chunks),
            func=func,
            expected_type=expected_type
        )

    def generate_data_chunks(self, lst: list) -> Generator[list, None, None]:
        total_chunks = ceil(len(lst) / self._chunk_size)
        n_chunks = total_chunks if self._max_chunks_number is None else min(total_chunks, self._max_chunks_number)

        for i in range(0, len(lst), self._chunk_size):
            print(f'Generating chunk {self._get_chunk_number(i)} out of {n_chunks} (Total: {total_chunks})')
            yield lst[i: i + self._chunk_size]

    def _get_chunk_number(self, index: int) -> int:
        chunk_number = (index / self._chunk_size) + 1
        return int(chunk_number)
