# PlanVenture API

旅行規劃應用程式的後端 API，使用 Flask 框架開發。

## 功能特色

- 用戶認證系統（註冊、登入）
- JWT Token 驗證
- 自動化 API 文檔（Swagger/OpenAPI）
- 資料庫 ORM（SQLAlchemy）
- **CORS 跨域支援（已配置用於 React 前端）**
- 完整的旅行管理 API

## 快速開始

### 🚀 一鍵啟動
```bash
./start.sh
```

### 手動設定

1. 創建虛擬環境：
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# 或
venv\Scripts\activate     # Windows
```

2. 安裝依賴項：
```bash
pip install -r requirements.txt
```

3. 環境變數設定：
```bash
cp .env.example .env
# 編輯 .env 檔案設定您的配置
```

4. 啟動 API：
```bash
python app.py
```

## 🌐 CORS 配置

本 API 已完整配置 CORS 以支援 React 前端，詳細說明請參考 [CORS_SETUP.md](CORS_SETUP.md)。

### 支援的前端 URL（開發環境）:
- `http://localhost:3000` (Create React App)
- `http://localhost:5173` (Vite)
- `http://localhost:3001` (備用端口)

### 測試 CORS 配置:
```bash
python test_cors.py
```
複製 `.sample.env` 為 `.env` 並根據需要修改設定。

### 資料庫設定

初始化資料庫表格：
```bash
python create_tables.py
```

### 啟動應用程式

```bash
python app.py
```


應用程式將在 `http://localhost:5001` 啟動。

## API 文檔


### Swagger UI

啟動應用程式後，可以訪問以下網址查看互動式 API 文檔：

- **Swagger UI**: http://localhost:5001/apidocs/
- **OpenAPI JSON**: http://localhost:5001/apispec_1.json


### 可用端點

#### 認證相關
- `POST /auth/register` - 用戶註冊
- `POST /auth/login` - 用戶登入

#### 一般端點
- `GET /` - 歡迎訊息
- `GET /health` - 健康檢查

#### 行程 (Trip) 相關
- `POST /api/trips` - 創建行程
- `GET /api/trips` - 取得所有行程
- `GET /api/trips/<trip_id>` - 取得單一行程
- `PUT /api/trips/<trip_id>` - 更新行程
- `DELETE /api/trips/<trip_id>` - 刪除行程
## Trip API 使用說明

### 認證
所有 Trip 端點皆需 JWT Token，請於 header 加入：

```
Authorization: Bearer <your-jwt-token>
```

### 主要端點範例

- **創建行程**：
  - `POST /api/trips`
  - 必填：destination, start_date, end_date (YYYY-MM-DD)
  - 可選：coordinates, itinerary (JSON)

- **取得所有行程**：
  - `GET /api/trips`

- **取得單一行程**：
  - `GET /api/trips/<trip_id>`

- **更新行程**：
  - `PUT /api/trips/<trip_id>`

- **刪除行程**：
  - `DELETE /api/trips/<trip_id>`

### 回應格式與錯誤處理

- 400 Bad Request：欄位缺漏或格式錯誤
- 401 Unauthorized：Token 無效或過期
- 404 Not Found：找不到行程
- 200/201：操作成功

### 測試

可直接執行 `test_trip_api.py` 進行自動化測試：

```bash
python test_trip_api.py
```

### 更完整的 Trip API 文件

請參考 `TRIP_API_DOCS.md` 取得所有欄位、範例與 curl/python 調用方式。

### 認證方式

API 使用 JWT (JSON Web Token) 進行認證。在需要認證的端點中，請在請求標頭中包含：

```
Authorization: Bearer <your-jwt-token>
```

## 專案結構

```
planventure-api/
├── app.py                 # 主應用程式檔案
├── requirements.txt       # Python 依賴項
├── create_tables.py       # 資料庫初始化腳本
├── .env                   # 環境變數設定
├── config/
│   └── swagger_config.py  # Swagger 配置
├── models/                # 資料模型
│   ├── __init__.py
│   ├── user.py           # 用戶模型
│   └── trip.py           # 行程模型
├── routes/                # 路由模組
│   └── auth.py           # 認證相關路由
├── utils/                 # 工具函數
│   ├── jwt_utils.py      # JWT 相關工具
│   └── password_utils.py # 密碼處理工具
├── instance/             # 實例檔案
│   └── planventure.db    # SQLite 資料庫
└── venv/                 # 虛擬環境（.gitignore）
```

## 開發指南

### 添加新的 API 端點

1. 在相應的路由模組中添加新的端點函數
2. 使用 Swagger 文檔字串格式添加 API 文檔：

```python
@blueprint.route('/example', methods=['POST'])
def example():
    """
    範例端點
    ---
    tags:
      - Example
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: "範例名稱"
    responses:
      200:
        description: 成功回應
        schema:
          type: object
          properties:
            message:
              type: string
              example: "操作成功"
    """
    # 端點邏輯
```

### Swagger 文檔最佳實踐

1. **使用標籤 (tags)**: 將相關的端點歸類到同一個標籤下
2. **詳細描述**: 提供清楚的端點描述和參數說明
3. **範例數據**: 在 schema 中包含範例值
4. **錯誤處理**: 記錄所有可能的回應狀態碼
5. **安全性**: 對需要認證的端點標註安全需求

## 貢獻指南

1. Fork 此專案
2. 創建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交變更 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟 Pull Request

## 授權

此專案使用 MIT 授權 - 查看 [LICENSE](LICENSE) 檔案了解詳情。
