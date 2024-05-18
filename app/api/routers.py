# -*- coding: utf-8 -*-
"""Routers for the API v1."""

from fastapi import APIRouter

from app.api.v1.paper import router as paper_router
from app.core.config import settings

v1_router = APIRouter(prefix=settings.API_V1_PREFIX)

v1_router.include_router(paper_router, prefix="/papers", tags=["papers"])
