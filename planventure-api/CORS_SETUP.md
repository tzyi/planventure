# CORS 配置指南

本專案已經配置好 CORS (Cross-Origin Resource Sharing)，以支援 React 前端應用程式。

## 🚀 快速開始

### 1. 安裝依賴
```bash
pip install -r requirements.txt
```

### 2. 環境配置
複製環境變數範例檔案：
```bash
cp .env.example .env
```

編輯 `.env` 檔案，根據需要調整配置。

### 3. 啟動 API 伺服器
```bash
python app.py
```

API 將在 `http://localhost:5001` 運行。

### 4. 測試 CORS 配置
```bash
python test_cors.py
```

## 🔧 CORS 配置選項

### 開發環境
預設允許以下來源：
- `http://localhost:3000` (React 預設端口)
- `http://localhost:3001` (備用端口)
- `http://localhost:5173` (Vite 預設端口)
- `http://127.0.0.1:3000`
- `http://127.0.0.1:3001`
- `http://127.0.0.1:5173`

### 生產環境
在 `.env` 檔案中設定 `FRONTEND_URL`：
```env
FRONTEND_URL=https://your-frontend-domain.com
```

### 寬鬆模式 (僅開發用)
如果需要允許所有來源 (僅用於開發)：
```env
FLASK_ENV=development
CORS_ALLOW_ALL=true
```

⚠️ **警告**: 寬鬆模式僅適用於開發環境，生產環境絕對不要使用！

## 🛠️ React 前端整合

### Fetch API 範例
```javascript
// GET 請求
fetch('http://localhost:5001/api/trips', {
  method: 'GET',
  credentials: 'include', // 包含認證資訊
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${token}`
  }
})
.then(response => response.json())
.then(data => console.log(data));

// POST 請求
fetch('http://localhost:5001/api/trips', {
  method: 'POST',
  credentials: 'include',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${token}`
  },
  body: JSON.stringify({
    title: '新旅行',
    description: '描述'
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

### Axios 範例
```javascript
import axios from 'axios';

// 建立 axios 實例
const api = axios.create({
  baseURL: 'http://localhost:5001',
  withCredentials: true, // 包含認證資訊
  headers: {
    'Content-Type': 'application/json'
  }
});

// 添加請求攔截器來自動添加 token
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// 使用範例
api.get('/api/trips')
  .then(response => console.log(response.data))
  .catch(error => console.error(error));
```

## 🔍 測試 CORS

### 手動測試
1. 啟動 Flask API (`python app.py`)
2. 在瀏覽器開發者工具中執行：
```javascript
fetch('http://localhost:5001/cors-test', {
  method: 'GET',
  headers: {
    'Origin': 'http://localhost:3000'
  }
})
.then(response => response.json())
.then(data => console.log(data));
```

### 自動化測試
執行 CORS 測試腳本：
```bash
python test_cors.py
```

## 📝 配置檔案說明

### `config/cors_config.py`
包含所有 CORS 配置選項：
- `CORS_CONFIG`: 生產環境配置
- `CORS_CONFIG_DEV`: 開發環境寬鬆配置
- `get_cors_config()`: 根據環境自動選擇配置

### 支援的配置選項
- **origins**: 允許的來源清單
- **methods**: 允許的 HTTP 方法
- **allow_headers**: 允許的請求標頭
- **expose_headers**: 暴露的回應標頭
- **supports_credentials**: 是否支援認證資訊
- **max_age**: 預檢請求快取時間

## 🔒 安全性建議

1. **生產環境**: 始終指定具體的允許來源，避免使用 `*`
2. **認證**: 使用 JWT token 進行 API 認證
3. **HTTPS**: 生產環境請使用 HTTPS
4. **標頭**: 只允許必要的請求標頭
5. **監控**: 監控 CORS 相關的錯誤和異常請求

## 🐛 常見問題

### CORS 錯誤
如果遇到 CORS 錯誤：
1. 檢查前端 URL 是否在允許清單中
2. 確認請求方法是否被允許
3. 檢查請求標頭是否正確
4. 查看瀏覽器開發者工具的網路面板

### 認證問題
如果認證相關功能不工作：
1. 確保設定了 `supports_credentials: True`
2. 前端請求要包含 `credentials: 'include'` 或 `withCredentials: true`
3. 檢查 JWT token 是否正確傳送

## 📞 支援

如有問題，請檢查：
1. Flask API 是否正常運行
2. 環境變數配置是否正確
3. 網路連接是否正常
4. 瀏覽器是否有快取問題
