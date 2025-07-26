"""
Swagger/OpenAPI 配置
"""

# Swagger 配置
SWAGGER_CONFIG = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger/"
}

# Swagger 模板
SWAGGER_TEMPLATE = {
    "swagger": "2.0",
    "info": {
        "title": "PlanVenture API",
        "description": "旅行規劃應用程式的 REST API。提供用戶認證、行程管理等功能。",
        "contact": {
            "responsibleOrganization": "PlanVenture Team",
            "responsibleDeveloper": "Developer",
            "email": "contact@planventure.com"
        },
        "termsOfService": "http://www.planventure.com/terms/",
        "version": "1.0.0"
    },
    "host": "localhost:5000",
    "basePath": "/",
    "schemes": [
        "http",
        "https"
    ],
    "consumes": [
        "application/json"
    ],
    "produces": [
        "application/json"
    ],
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "JWT Authorization header using the Bearer scheme. Example: \"Authorization: Bearer {token}\""
        }
    },
    "definitions": {
        "User": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer",
                    "description": "用戶唯一識別碼"
                },
                "email": {
                    "type": "string",
                    "format": "email",
                    "description": "用戶電子郵件地址"
                },
                "created_at": {
                    "type": "string",
                    "format": "date-time",
                    "description": "用戶創建時間"
                },
                "updated_at": {
                    "type": "string",
                    "format": "date-time",
                    "description": "用戶最後更新時間"
                }
            }
        },
        "Error": {
            "type": "object",
            "properties": {
                "error": {
                    "type": "string",
                    "description": "錯誤訊息"
                }
            }
        },
        "AuthResponse": {
            "type": "object",
            "properties": {
                "message": {
                    "type": "string",
                    "description": "操作結果訊息"
                },
                "token": {
                    "type": "string",
                    "description": "JWT 訪問令牌"
                },
                "user": {
                    "$ref": "#/definitions/User"
                }
            }
        }
    }
}
