"""Mischellaneous utilities for unittest codes"""

import importlib
from unittest.mock import patch


def patch_method(method_object: object):
    """Patch a method of the target.

    This method is responsible for patching a method of the target.

    Args:
        method_object (object): The method object.

    Returns:
        Any: The patched method.

    """

    target_class_name, method_name = method_object.__qualname__.split(".", maxsplit=-1)
    module_name = method_object.__module__
    target_class_obj = getattr(importlib.import_module(module_name), target_class_name)

    return patch.object(target_class_obj, method_name)
