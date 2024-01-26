from typing import Any, List, Sized, Optional, Type

from genie_common.tools.logs import logger
from genie_common.typing import F
from tqdm import tqdm


class SyncPoolExecutor:
    def __init__(self, validate_results: bool = True):
        self._validate_results = validate_results

    def run(self,
            iterable: Sized,
            func: F,
            expected_type: Optional[Type] = None) -> List[Any]:
        results = self._execute(iterable, func)

        if self._validate_results:
            return self._filter_out_invalid_results(results, expected_type)

        return results

    def _execute(self, iterable: Sized, func: F) -> List[Any]:
        results = []

        with tqdm(total=len(iterable)) as progress_bar:
            for value in iterable:
                result = self._execute_single(func, value, progress_bar)
                results.append(result)

        return results

    @staticmethod
    def _execute_single(func: F, value: Any, progress_bar: tqdm) -> Any:
        try:
            return func(value)

        except Exception as e:
            logger.exception("PoolExecutor encountered exception")
            return e

        finally:
            progress_bar.update(1)

    @staticmethod
    def _filter_out_invalid_results(results: List[Any], expected_type: Type) -> List[Any]:
        valid_results = [result for result in results if isinstance(result, expected_type)]
        logger.info(f"Successfully retrieved {len(valid_results)} valid results out of {len(results)} total requests")

        return valid_results
