from typing import List

from app.settings import settings

MODELS_MODULES: List[str] = [
    "app.db.models.drivers",
    "app.db.models.grand_prix",
    "app.db.models.session_types",
    "app.db.models.sessions",
    "app.db.models.teams",
]

TORTOISE_ORM = {
    "connections": {
        "default": settings.db_url,
    },
    "apps": {
        "models": {
            "models": MODELS_MODULES,
            "default_connection": "default",
        },
    },
}
