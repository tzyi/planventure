# Trip Routes API Documentation

本文檔描述了 PlanVenture API 中的 Trip 路由端點，提供完整的 CRUD 操作。

## 基礎信息

- **基礎 URL**: `http://localhost:5001/api`
- **認證方式**: Bearer Token (JWT)
- **Content-Type**: `application/json`

## 認證

所有 Trip API 端點都需要認證。在請求頭中包含 JWT token：

```
Authorization: Bearer <your-jwt-token>
```

## API 端點

### 1. 創建行程

**POST** `/trips`

創建一個新的行程。

#### 請求體
```json
{
  "destination": "東京",
  "start_date": "2024-04-01",
  "end_date": "2024-04-07",
  "coordinates": {
    "lat": 35.6762,
    "lng": 139.6503
  },
  "itinerary": [
    {
      "day": 1,
      "plan": "抵達成田機場，前往飯店"
    },
    {
      "day": 2,
      "plan": "參觀淺草寺和雷門"
    }
  ]
}
```

#### 必填字段
- `destination` (string): 目的地
- `start_date` (string): 開始日期，格式：YYYY-MM-DD
- `end_date` (string): 結束日期，格式：YYYY-MM-DD

#### 可選字段
- `coordinates` (object): 座標信息
  - `lat` (number): 緯度
  - `lng` (number): 經度
- `itinerary` (array): 行程規劃數組

#### 響應
```json
{
  "message": "Trip created successfully",
  "trip": {
    "id": 1,
    "destination": "東京",
    "start_date": "2024-04-01",
    "end_date": "2024-04-07",
    "coordinates": {...},
    "itinerary": [...]
  }
}
```

### 2. 獲取所有行程

**GET** `/trips`

獲取當前用戶的所有行程。

#### 響應
```json
{
  "trips": [
    {
      "id": 1,
      "destination": "東京",
      "start_date": "2024-04-01",
      "end_date": "2024-04-07",
      "coordinates": {...},
      "itinerary": [...]
    }
  ]
}
```

### 3. 獲取特定行程

**GET** `/trips/{trip_id}`

獲取指定 ID 的行程詳情。

#### 路徑參數
- `trip_id` (integer): 行程 ID

#### 響應
```json
{
  "trip": {
    "id": 1,
    "destination": "東京",
    "start_date": "2024-04-01",
    "end_date": "2024-04-07",
    "coordinates": {...},
    "itinerary": [...]
  }
}
```

### 4. 更新行程

**PUT** `/trips/{trip_id}`

更新指定 ID 的行程。

#### 路徑參數
- `trip_id` (integer): 行程 ID

#### 請求體
可以包含任何需要更新的字段：
```json
{
  "destination": "京都",
  "start_date": "2024-04-01",
  "end_date": "2024-04-08",
  "coordinates": {
    "lat": 35.0116,
    "lng": 135.7681
  },
  "itinerary": [
    {
      "day": 1,
      "plan": "抵達關西機場，前往京都"
    }
  ]
}
```

#### 響應
```json
{
  "message": "Trip updated successfully",
  "trip": {
    "id": 1,
    "destination": "京都",
    "start_date": "2024-04-01",
    "end_date": "2024-04-08",
    "coordinates": {...},
    "itinerary": [...]
  }
}
```

### 5. 刪除行程

**DELETE** `/trips/{trip_id}`

刪除指定 ID 的行程。

#### 路徑參數
- `trip_id` (integer): 行程 ID

#### 響應
```json
{
  "message": "Trip deleted successfully"
}
```

## 錯誤響應

### 400 Bad Request
```json
{
  "msg": "Missing required field: destination"
}
```

### 401 Unauthorized
```json
{
  "msg": "Invalid or expired token"
}
```

### 404 Not Found
```json
{
  "msg": "Trip not found"
}
```

### 500 Internal Server Error
```json
{
  "msg": "Error creating trip: [error message]"
}
```

## 數據驗證

### 日期格式
- 日期必須使用 YYYY-MM-DD 格式
- 結束日期必須晚於開始日期

### 必填字段驗證
- `destination`: 不能為空
- `start_date`: 必須是有效的日期格式
- `end_date`: 必須是有效的日期格式

## 使用示例

### 使用 curl 創建行程

```bash
curl -X POST http://localhost:5001/api/trips \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "destination": "東京",
    "start_date": "2024-04-01",
    "end_date": "2024-04-07",
    "coordinates": {
      "lat": 35.6762,
      "lng": 139.6503
    },
    "itinerary": [
      {
        "day": 1,
        "plan": "抵達成田機場，前往飯店"
      }
    ]
  }'
```

### 使用 Python requests

```python
import requests

headers = {
    'Authorization': 'Bearer YOUR_JWT_TOKEN',
    'Content-Type': 'application/json'
}

trip_data = {
    "destination": "東京",
    "start_date": "2024-04-01",
    "end_date": "2024-04-07",
    "coordinates": {
        "lat": 35.6762,
        "lng": 139.6503
    },
    "itinerary": [
        {
            "day": 1,
            "plan": "抵達成田機場，前往飯店"
        }
    ]
}

response = requests.post(
    'http://localhost:5001/api/trips',
    json=trip_data,
    headers=headers
)

print(response.json())
```

## 測試

項目包含完整的測試腳本 `test_trip_api.py`，可以測試所有 API 端點：

```bash
# 啟動 Flask 應用
python app.py

# 在另一個終端運行測試
python test_trip_api.py
```

## Swagger 文檔

API 文檔也可以通過 Swagger UI 查看：
http://localhost:5001/apidocs/
