"""Base model for all models to inherit from"""

from beanie import Document

from app.utils.registry import Registry

DOCUMENT_REGISTRY = Registry("model", Document)
