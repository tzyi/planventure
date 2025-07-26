#!/usr/bin/env python3
"""
API 測試腳本
測試 PlanVenture API 的基本功能
"""

import requests
import json

BASE_URL = "http://localhost:5000"

def test_health_check():
    """測試健康檢查端點"""
    print("=== 測試健康檢查 ===")
    response = requests.get(f"{BASE_URL}/health")
    print(f"狀態碼: {response.status_code}")
    print(f"回應: {response.json()}")
    print()

def test_home():
    """測試首頁端點"""
    print("=== 測試首頁 ===")
    response = requests.get(f"{BASE_URL}/")
    print(f"狀態碼: {response.status_code}")
    print(f"回應: {response.json()}")
    print()

def test_swagger_spec():
    """測試 Swagger API 規格"""
    print("=== 測試 Swagger API 規格 ===")
    response = requests.get(f"{BASE_URL}/apispec_1.json")
    print(f"狀態碼: {response.status_code}")
    if response.status_code == 200:
        spec = response.json()
        print(f"API 標題: {spec['info']['title']}")
        print(f"API 版本: {spec['info']['version']}")
        print(f"可用端點: {list(spec.get('paths', {}).keys())}")
    print()

def test_register():
    """測試用戶註冊"""
    print("=== 測試用戶註冊 ===")
    test_user = {
        "email": "test@example.com",
        "password": "testpassword123"
    }
    response = requests.post(
        f"{BASE_URL}/auth/register",
        json=test_user,
        headers={"Content-Type": "application/json"}
    )
    print(f"狀態碼: {response.status_code}")
    print(f"回應: {response.json()}")
    
    if response.status_code == 201:
        return response.json().get('token')
    print()

def test_login():
    """測試用戶登入"""
    print("=== 測試用戶登入 ===")
    login_data = {
        "email": "test@example.com",
        "password": "testpassword123"
    }
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json=login_data,
        headers={"Content-Type": "application/json"}
    )
    print(f"狀態碼: {response.status_code}")
    print(f"回應: {response.json()}")
    
    if response.status_code == 200:
        return response.json().get('token')
    print()

def main():
    """主測試函數"""
    print("開始 API 測試...\n")
    
    try:
        # 基本端點測試
        test_health_check()
        test_home()
        test_swagger_spec()
        
        # 認證測試
        token = test_register()
        if not token:
            # 如果註冊失敗（可能用戶已存在），嘗試登入
            token = test_login()
        
        if token:
            print(f"獲得 JWT Token: {token[:50]}...")
        
        print("API 測試完成！")
        print(f"\n可以訪問 Swagger UI: {BASE_URL}/swagger/")
        
    except requests.exceptions.ConnectionError:
        print("錯誤: 無法連接到 API 伺服器")
        print("請確保 Flask 應用程式正在運行於 http://localhost:5000")
    except Exception as e:
        print(f"測試過程中發生錯誤: {e}")

if __name__ == "__main__":
    main()
