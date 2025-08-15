# app/core/openapi.py

"""
The custom_openapi() function overrides FastAPI’s default OpenAPI schema generation to include JWT Bearer authentication in the Swagger (docs) UI. It defines a bearerAuth security scheme using the HTTP Authorization header and attaches this requirement to every API route in the schema. This enables the "Authorize" button in Swagger UI, allowing users to input a JWT token once and automatically include it in requests to protected endpoints. The function caches the schema for performance by storing it in app.openapi_schema.
"""

from fastapi.openapi.utils import get_openapi

def custom_openapi(app):
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="My Blog API",
        version="1.0.0",
        description="API with JWT authentication using Bearer tokens. Use the 'Authorize' button to authenticate requests.",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "bearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }

    for path in openapi_schema["paths"].values():
        for method in path.values():
            method.setdefault("security", [{"bearerAuth": []}])

    app.openapi_schema = openapi_schema
    return app.openapi_schema
