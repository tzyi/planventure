#!/usr/bin/env python3
"""
Trip API 測試腳本
此腳本用於測試所有 Trip 相關的 API 端點
"""

import requests
import json
from datetime import datetime, timedelta

# API 基礎 URL
BASE_URL = "http://localhost:5001"

def test_trip_crud():
    """測試 Trip CRUD 操作"""
    
    # 1. 首先註冊一個測試用戶
    print("=== 1. 註冊測試用戶 ===")
    register_data = {
        "email": "test_trip@example.com",
        "password": "testpassword123"
    }
    
    response = requests.post(f"{BASE_URL}/auth/register", json=register_data)
    print(f"註冊響應: {response.status_code}")
    print(f"註冊內容: {response.json()}")
    
    # 2. 登入獲取 token
    print("\n=== 2. 用戶登入 ===")
    login_data = {
        "email": "test_trip@example.com",
        "password": "testpassword123"
    }
    
    response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
    print(f"登入響應: {response.status_code}")
    login_result = response.json()
    print(f"登入內容: {login_result}")
    
    if response.status_code != 200:
        print("登入失敗，停止測試")
        return
    
    # 獲取 access token
    access_token = login_result.get('token')  # 改為使用 'token' 而不是 'access_token'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    # 3. 創建行程
    print("\n=== 3. 創建行程 ===")
    trip_data = {
        "destination": "東京",
        "start_date": "2024-04-01",
        "end_date": "2024-04-07",
        "coordinates": {
            "lat": 35.6762,
            "lng": 139.6503
        },
        "itinerary": [
            {"day": 1, "plan": "抵達成田機場，前往飯店"},
            {"day": 2, "plan": "參觀淺草寺和雷門"},
            {"day": 3, "plan": "東京迪士尼樂園"}
        ]
    }
    
    response = requests.post(f"{BASE_URL}/api/trips", json=trip_data, headers=headers)
    print(f"創建行程響應: {response.status_code}")
    create_result = response.json()
    print(f"創建行程內容: {json.dumps(create_result, indent=2, ensure_ascii=False)}")
    
    if response.status_code != 201:
        print("創建行程失敗，停止測試")
        return
    
    trip_id = create_result.get('trip', {}).get('id')
    print(f"創建的行程 ID: {trip_id}")
    
    # 4. 獲取所有行程
    print("\n=== 4. 獲取所有行程 ===")
    response = requests.get(f"{BASE_URL}/api/trips", headers=headers)
    print(f"獲取行程響應: {response.status_code}")
    trips_result = response.json()
    print(f"所有行程: {json.dumps(trips_result, indent=2, ensure_ascii=False)}")
    
    # 5. 獲取特定行程
    print(f"\n=== 5. 獲取特定行程 (ID: {trip_id}) ===")
    response = requests.get(f"{BASE_URL}/api/trips/{trip_id}", headers=headers)
    print(f"獲取特定行程響應: {response.status_code}")
    trip_result = response.json()
    print(f"特定行程內容: {json.dumps(trip_result, indent=2, ensure_ascii=False)}")
    
    # 6. 更新行程
    print(f"\n=== 6. 更新行程 (ID: {trip_id}) ===")
    update_data = {
        "destination": "京都",
        "start_date": "2024-04-01",
        "end_date": "2024-04-08",
        "coordinates": {
            "lat": 35.0116,
            "lng": 135.7681
        },
        "itinerary": [
            {"day": 1, "plan": "抵達關西機場，前往京都"},
            {"day": 2, "plan": "參觀清水寺"},
            {"day": 3, "plan": "金閣寺和銀閣寺"},
            {"day": 4, "plan": "伏見稻荷大社"}
        ]
    }
    
    response = requests.put(f"{BASE_URL}/api/trips/{trip_id}", json=update_data, headers=headers)
    print(f"更新行程響應: {response.status_code}")
    update_result = response.json()
    print(f"更新行程內容: {json.dumps(update_result, indent=2, ensure_ascii=False)}")
    
    # 7. 再次獲取行程確認更新
    print(f"\n=== 7. 確認行程已更新 (ID: {trip_id}) ===")
    response = requests.get(f"{BASE_URL}/api/trips/{trip_id}", headers=headers)
    print(f"確認更新響應: {response.status_code}")
    updated_trip = response.json()
    print(f"更新後的行程: {json.dumps(updated_trip, indent=2, ensure_ascii=False)}")
    
    # 8. 創建第二個行程
    print("\n=== 8. 創建第二個行程 ===")
    trip_data_2 = {
        "destination": "大阪",
        "start_date": "2024-05-01",
        "end_date": "2024-05-05",
        "coordinates": {
            "lat": 34.6937,
            "lng": 135.5023
        },
        "itinerary": [
            {"day": 1, "plan": "大阪城"},
            {"day": 2, "plan": "環球影城"}
        ]
    }
    
    response = requests.post(f"{BASE_URL}/api/trips", json=trip_data_2, headers=headers)
    print(f"創建第二個行程響應: {response.status_code}")
    create_result_2 = response.json()
    print(f"第二個行程內容: {json.dumps(create_result_2, indent=2, ensure_ascii=False)}")
    
    trip_id_2 = create_result_2.get('trip', {}).get('id')
    
    # 9. 獲取所有行程（應該有兩個）
    print("\n=== 9. 獲取所有行程（應該有兩個） ===")
    response = requests.get(f"{BASE_URL}/api/trips", headers=headers)
    print(f"獲取所有行程響應: {response.status_code}")
    all_trips = response.json()
    print(f"所有行程數量: {len(all_trips.get('trips', []))}")
    print(f"所有行程: {json.dumps(all_trips, indent=2, ensure_ascii=False)}")
    
    # 10. 刪除第一個行程
    print(f"\n=== 10. 刪除行程 (ID: {trip_id}) ===")
    response = requests.delete(f"{BASE_URL}/api/trips/{trip_id}", headers=headers)
    print(f"刪除行程響應: {response.status_code}")
    delete_result = response.json()
    print(f"刪除結果: {delete_result}")
    
    # 11. 確認行程已刪除
    print(f"\n=== 11. 確認行程已刪除 (ID: {trip_id}) ===")
    response = requests.get(f"{BASE_URL}/api/trips/{trip_id}", headers=headers)
    print(f"嘗試獲取已刪除行程響應: {response.status_code}")
    print(f"響應內容: {response.json()}")
    
    # 12. 最終獲取所有行程（應該只剩一個）
    print("\n=== 12. 最終獲取所有行程（應該只剩一個） ===")
    response = requests.get(f"{BASE_URL}/api/trips", headers=headers)
    print(f"最終獲取響應: {response.status_code}")
    final_trips = response.json()
    print(f"最終行程數量: {len(final_trips.get('trips', []))}")
    print(f"最終行程: {json.dumps(final_trips, indent=2, ensure_ascii=False)}")

def test_error_cases():
    """測試錯誤情況"""
    print("\n" + "="*50)
    print("測試錯誤情況")
    print("="*50)
    
    # 1. 無效的 token
    print("\n=== 1. 測試無效 token ===")
    invalid_headers = {
        'Authorization': 'Bearer invalid_token',
        'Content-Type': 'application/json'
    }
    
    response = requests.get(f"{BASE_URL}/api/trips", headers=invalid_headers)
    print(f"無效 token 響應: {response.status_code}")
    print(f"響應內容: {response.json()}")
    
    # 2. 缺少必填欄位
    print("\n=== 2. 測試缺少必填欄位 ===")
    # 先獲取有效 token
    login_data = {
        "email": "test_trip@example.com",
        "password": "testpassword123"
    }
    
    response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
    if response.status_code == 200:
        access_token = response.json().get('token')  # 改為使用 'token'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        
        incomplete_data = {
            "destination": "測試地點"
            # 缺少 start_date 和 end_date
        }
        
        response = requests.post(f"{BASE_URL}/api/trips", json=incomplete_data, headers=headers)
        print(f"缺少必填欄位響應: {response.status_code}")
        print(f"響應內容: {response.json()}")
        
        # 3. 無效日期格式
        print("\n=== 3. 測試無效日期格式 ===")
        invalid_date_data = {
            "destination": "測試地點",
            "start_date": "2024-13-01",  # 無效月份
            "end_date": "2024-04-07"
        }
        
        response = requests.post(f"{BASE_URL}/api/trips", json=invalid_date_data, headers=headers)
        print(f"無效日期格式響應: {response.status_code}")
        print(f"響應內容: {response.json()}")
        
        # 4. 結束日期早於開始日期
        print("\n=== 4. 測試結束日期早於開始日期 ===")
        invalid_date_logic = {
            "destination": "測試地點",
            "start_date": "2024-04-07",
            "end_date": "2024-04-01"  # 結束日期早於開始日期
        }
        
        response = requests.post(f"{BASE_URL}/api/trips", json=invalid_date_logic, headers=headers)
        print(f"日期邏輯錯誤響應: {response.status_code}")
        print(f"響應內容: {response.json()}")
        
        # 5. 獲取不存在的行程
        print("\n=== 5. 測試獲取不存在的行程 ===")
        response = requests.get(f"{BASE_URL}/api/trips/99999", headers=headers)
        print(f"獲取不存在行程響應: {response.status_code}")
        print(f"響應內容: {response.json()}")

if __name__ == "__main__":
    print("開始測試 Trip API...")
    print("請確保服務器正在運行在 http://localhost:5001")
    
    try:
        # 測試基本連接
        response = requests.get(f"{BASE_URL}/")
        if response.status_code != 200:
            print("無法連接到服務器")
            exit(1)
        
        print("服務器連接成功，開始測試...")
        
        # 執行主要的 CRUD 測試
        test_trip_crud()
        
        # 執行錯誤情況測試
        test_error_cases()
        
        print("\n" + "="*50)
        print("所有測試完成！")
        print("="*50)
        
    except requests.exceptions.ConnectionError:
        print("錯誤：無法連接到服務器。請確保 Flask 應用正在運行。")
    except Exception as e:
        print(f"測試過程中發生錯誤: {str(e)}")
