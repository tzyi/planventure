#!/bin/bash

# PlanVenture API 啟動腳本

echo "🚀 啟動 PlanVenture API..."

# 檢查虛擬環境是否存在
if [ ! -d "venv" ]; then
    echo "📦 創建虛擬環境..."
    python3 -m venv venv
fi

# 啟動虛擬環境
echo "🔧 啟動虛擬環境..."
source venv/bin/activate

# 安裝依賴 (如果需要)
echo "📚 檢查並安裝依賴..."
pip install -r requirements.txt

# 檢查環境變數檔案
if [ ! -f ".env" ]; then
    echo "⚠️  .env 檔案不存在，複製範例檔案..."
    cp .env.example .env
    echo "✏️  請編輯 .env 檔案設定您的配置"
fi

# 啟動應用程式
echo "🌟 啟動 Flask API (按 Ctrl+C 停止)..."
echo "📍 API 將在 http://localhost:5001 運行"
echo "📄 API 文件: http://localhost:5001/apidocs"
echo ""

python app.py
