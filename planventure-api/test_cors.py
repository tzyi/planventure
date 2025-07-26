"""
CORS 配置測試腳本
用於測試 Flask API 的 CORS 配置是否正確
"""

import requests
import json

# API 基礎 URL
API_BASE_URL = "http://localhost:5001"

def test_cors_preflight():
    """測試 CORS 預檢請求"""
    print("🔍 測試 CORS 預檢請求...")
    
    # 模擬瀏覽器的預檢請求
    headers = {
        'Origin': 'http://localhost:3000',
        'Access-Control-Request-Method': 'POST',
        'Access-Control-Request-Headers': 'Content-Type,Authorization'
    }
    
    try:
        response = requests.options(f"{API_BASE_URL}/cors-test", headers=headers)
        print(f"狀態碼: {response.status_code}")
        print(f"回應標頭: {dict(response.headers)}")
        
        # 檢查重要的 CORS 標頭
        cors_headers = {
            'Access-Control-Allow-Origin': response.headers.get('Access-Control-Allow-Origin'),
            'Access-Control-Allow-Methods': response.headers.get('Access-Control-Allow-Methods'),
            'Access-Control-Allow-Headers': response.headers.get('Access-Control-Allow-Headers'),
            'Access-Control-Allow-Credentials': response.headers.get('Access-Control-Allow-Credentials')
        }
        
        print("\n📋 CORS 標頭檢查:")
        for header, value in cors_headers.items():
            status = "✅" if value else "❌"
            print(f"{status} {header}: {value}")
            
    except Exception as e:
        print(f"❌ 預檢請求失敗: {e}")

def test_cors_actual_request():
    """測試實際的 CORS 請求"""
    print("\n🔍 測試實際 CORS 請求...")
    
    headers = {
        'Origin': 'http://localhost:3000',
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.get(f"{API_BASE_URL}/cors-test", headers=headers)
        print(f"狀態碼: {response.status_code}")
        print(f"回應內容: {response.json()}")
        
        # 檢查 CORS 標頭
        origin_header = response.headers.get('Access-Control-Allow-Origin')
        credentials_header = response.headers.get('Access-Control-Allow-Credentials')
        
        print(f"\n📋 CORS 回應標頭:")
        print(f"✅ Access-Control-Allow-Origin: {origin_header}")
        print(f"✅ Access-Control-Allow-Credentials: {credentials_header}")
        
    except Exception as e:
        print(f"❌ 實際請求失敗: {e}")

def test_api_endpoints():
    """測試主要 API 端點的 CORS"""
    print("\n🔍 測試主要 API 端點...")
    
    endpoints = [
        "/",
        "/health",
        "/cors-test"
    ]
    
    headers = {
        'Origin': 'http://localhost:3000'
    }
    
    for endpoint in endpoints:
        try:
            response = requests.get(f"{API_BASE_URL}{endpoint}", headers=headers)
            status = "✅" if response.status_code == 200 else "❌"
            print(f"{status} {endpoint}: 狀態碼 {response.status_code}")
        except Exception as e:
            print(f"❌ {endpoint}: 請求失敗 - {e}")

if __name__ == "__main__":
    print("🚀 開始 CORS 配置測試\n")
    print("請確保 Flask API 正在 http://localhost:5001 運行\n")
    
    test_cors_preflight()
    test_cors_actual_request()
    test_api_endpoints()
    
    print("\n✅ CORS 測試完成!")
    print("\n💡 如果看到任何 ❌ 標記，請檢查:")
    print("1. Flask API 是否正在運行")
    print("2. CORS 配置是否正確")
    print("3. 防火牆或代理設定")
