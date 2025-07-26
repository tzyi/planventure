"""
CORS 配置設定
用於配置 Flask-CORS 以支援 React 前端應用程式
"""

import os

# 根據環境變數決定允許的來源
def get_allowed_origins():
    """
    取得允許的來源列表
    在生產環境中，請設定 FRONTEND_URL 環境變數
    """
    # 從環境變數讀取前端 URL
    frontend_url = os.getenv('FRONTEND_URL')
    
    if frontend_url:
        # 生產環境 - 使用環境變數中的 URL
        return [frontend_url]
    else:
        # 開發環境 - 允許常見的本地開發端口
        return [
            "http://localhost:3000",  # React 預設開發端口
            "http://localhost:3001",  # 備用端口
            "http://127.0.0.1:3000",
            "http://127.0.0.1:3001",
            "http://localhost:5173",  # Vite 預設端口
            "http://127.0.0.1:5173"
        ]

# CORS 配置
CORS_CONFIG = {
    # 允許的來源
    "origins": get_allowed_origins(),
    
    # 允許的 HTTP 方法
    "methods": [
        "GET", 
        "POST", 
        "PUT", 
        "DELETE", 
        "OPTIONS", 
        "PATCH"
    ],
    
    # 允許的請求標頭
    "allow_headers": [
        "Content-Type",
        "Authorization", 
        "Access-Control-Allow-Credentials",
        "Access-Control-Allow-Origin",
        "X-Requested-With",
        "Accept",
        "Origin"
    ],
    
    # 允許的回應標頭
    "expose_headers": [
        "Content-Range",
        "X-Content-Range",
        "Authorization"
    ],
    
    # 允許攜帶認證資訊 (cookies, authorization headers)
    "supports_credentials": True,
    
    # 預檢請求的快取時間 (秒)
    "max_age": 600
}

# 開發環境的寬鬆配置 (僅在開發時使用)
CORS_CONFIG_DEV = {
    "origins": "*",  # 允許所有來源 (僅開發用)
    "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    "allow_headers": "*",
    "supports_credentials": False,  # 使用 * 時不能為 True
    "max_age": 600
}

def get_cors_config():
    """
    根據環境回傳適當的 CORS 配置
    """
    # 檢查是否為開發環境
    if os.getenv('FLASK_ENV') == 'development' and os.getenv('CORS_ALLOW_ALL') == 'true':
        return CORS_CONFIG_DEV
    else:
        return CORS_CONFIG
