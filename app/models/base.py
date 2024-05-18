# -*- coding: utf-8 -*-
"""Base model for all models to inherit from"""

from beanie import Document

from app.common.registry import Registry

DOCUMENT_REGISTRY = Registry("model", Document)
