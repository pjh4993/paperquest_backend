# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
"""Registry module.

This module contains the registry class.

"""

from typing import Dict, Iterable, Iterator, Tuple, TypeVar

from tabulate import tabulate

T = TypeVar("T")


class Registry(Iterable[Tuple[str, type[T]]]):
    """
    The registry that provides name -> object mapping, to support third-party
    users' custom modules.

    """

    def __init__(self, name: str, obj_type: type[T]) -> None:
        """Initialize the registry.

        Args:
            name (str): the name of this registry

        """
        self._name: str = name
        self._obj_map: Dict[str, type[obj_type]] = {}

    def _do_register(self, name: str, obj: type[T]) -> None:
        """Register object to obj map.

        Args:
            name (str): the name of the object
            obj (type[T]): the object to be registered

        """

        assert (
            name not in self._obj_map
        ), f"An object named '{name}' was already registered in '{self._name}' registry!"
        self._obj_map[name] = obj

    def register(self, obj: type[T]) -> type[T]:
        """Register object decorator

        Register the given object under the the name `obj.__name__`.
        Can be used as either a decorator or not. See docstring of this class for usage.

        Args:
            obj (Optional[type[T]]): the object to be registered

        """

        self._do_register(obj.__name__, obj)
        return obj

    def get(self, name: str) -> type[T]:
        """Get object by name.

        Args:
            name (str): the name of the object

        Returns:
            type[T]: the object

        """

        ret = self._obj_map.get(name)
        if ret is None:
            raise KeyError(f"No object named '{name}' found in '{self._name}' registry!")
        return ret

    def __contains__(self, name: str) -> bool:
        return name in self._obj_map

    def __repr__(self) -> str:
        table_headers = ["Names", "Objects"]
        table = tabulate(self._obj_map.items(), headers=table_headers, tablefmt="fancy_grid")
        return f"Registry of {self._name}:\n" + table

    def __iter__(self) -> Iterator[Tuple[str, type[T]]]:
        return iter(self._obj_map.items())

    __str__ = __repr__
