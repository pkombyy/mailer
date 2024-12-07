from .start import router as start_router
from .email import router as email_router
from .admin import router as admin_router

__all__ = [
    "start_router",
    "email_router",
    "admin_router",
]