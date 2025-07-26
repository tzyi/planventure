# Planventure Client

This is the frontend client application for PlanVenture, built with React and Vite.

## Overview

PlanVenture client is a modern web application that provides an interactive interface for planning and managing travel adventures.

## Getting Started

### Prerequisites

- Node.js (v18 or higher)
- npm v8 or higher

### Installation

1. Fork and Clone the repository
2. Navigate to the client directory:
    ```bash
    cd planventure-client
    ```
3. Install dependencies:
    ```bash
    npm install
    ```
4. Start the development server:
    ```bash
    npm run dev
    ```

## Available Scripts

- `npm run dev` - Runs the app in development mode with Vite
- `npm run build` - Builds the app for production
- `npm run preview` - Preview the production build locally
- `npm run lint` - Lint the codebase using ESLint

## Technologies Used

- React 18
- Vite
- React Router DOM
- Material UI (MUI)
- Emotion for styling
- ESLint for code quality


## Dir

```bash
planventure-client/
├── .gitignore                # Git 忽略規則
├── eslint.config.js          # ESLint 設定檔
├── index.html                # 前端入口 HTML
├── package.json              # npm 專案描述與依賴
├── README.md                 # 專案說明文件
├── vite.config.js            # Vite 打包工具設定
├── public/                   # 靜態資源（favicon、manifest 等）
│   └── ...                   # 各種圖片與網站設定檔
└── src/                      # 前端原始碼目錄
    ├── App.css               # 全域樣式
    ├── App.jsx               # React 主要進入點
    ├── index.css             # 其他全域 CSS
    ├── main.jsx              # React 應用程式啟動點
    ├── theme.js              # MUI 主題設定
    ├── assets/               # 前端用到的圖片、SVG 等
    ├── components/           # 可重用的 React 元件
    │   ├── auth/             # 登入、註冊相關元件
    │   ├── itinerary/        # 行程規劃相關元件
    │   ├── navigation/       # 導覽列、頁尾等
    │   ├── overview/         # 行程總覽相關元件
    │   ├── routing/          # 路由守衛等
    │   └── trips/            # 旅程列表、卡片等
    ├── context/              # React Context（如 AuthContext）
    ├── data/                 # 靜態資料或模板
    ├── layouts/              # 頁面佈局元件（如 MainLayout, DashboardLayout）
    ├── pages/                # 各個頁面元件（如首頁、登入、儀表板、旅程詳情等）
    ├── routes/               # 路由設定
    └── services/             # API 請求相關服務（如 tripService, api）
```
### 主要說明

public/：放置靜態檔案，這些檔案會直接被複製到 build 目錄，通常用於 favicon、manifest、logo 等。

src/：所有 React 原始碼都在這裡，包含元件、頁面、佈局、API 服務、主題設定等。

components/：細分多個子資料夾，依照功能分類元件，方便維護與重用。

layouts/：定義不同頁面的外框架（如有側邊欄、導覽列等）。

pages/：每個頁面一個元件，對應路由。

services/：與後端 API 溝通的邏輯集中於此。

context/：全域狀態管理（如登入狀態）。

data/：靜態資料或模板（如行程模板）。

routes/：集中管理所有路由設定。

assets/：圖片、SVG 等靜態資源。


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.