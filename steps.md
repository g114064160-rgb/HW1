# 專案執行步驟 (steps.md)

本文件記錄了專案從初始化到部署到 GitHub 的主要步驟。

## 1. 專案初始化與檔案準備
- 專案目錄 `C:\Users\user\Desktop\HW1` 包含 `app.py` 和 `simple_linear_regression.py`。
- 確認 `app.py` 為 Streamlit 應用程式。

## 2. Git 儲存庫設定
- 在專案根目錄初始化 Git 儲存庫：`git init -b main`。
- 設定 Git 使用者名稱和電子郵件 (使用預設值 `user` 和 `user@example.com`)。
- 將所有現有檔案加入暫存區並提交：`git add .` 和 `git commit -m "Initial commit"`。
- 添加遠端 GitHub 儲存庫：`git remote add origin https://github.com/g114064160-rgb/HW1.git`。
- 將本地提交推送到 GitHub：`git push -u origin main`。

## 3. 依賴安裝
- 確認 Streamlit 及相關 Python 函式庫 (`scikit-learn`, `pandas`, `matplotlib`, `numpy`) 已安裝。
- 建議的安裝命令：`pip install streamlit scikit-learn pandas matplotlib numpy`。

## 4. 運行 Streamlit 應用程式
- 指導使用者在本地運行 Streamlit 應用程式：`python -m streamlit run app.py`。
- 解釋 `streamlit` 命令無法直接執行的原因 (PATH 環境變數問題)，並提供 `python -m` 的解決方案。

## 5. 文件撰寫與更新
- 撰寫 `README.md`：提供專案概述、運行指南和檔案結構。
- 撰寫 `log.md`：記錄專案開發日誌。
- 撰寫 `process_summary.md`：總結 CRISP-DM 流程。
- 撰寫 `requirements.txt`：列出所有 Python 依賴。
- 撰寫 `steps.md`：記錄專案執行步驟。

## 6. 更新 GitHub 儲存庫
- 將所有新建立的 `.md` 和 `requirements.txt` 檔案加入暫存區。
- 提交這些新檔案。
- 將新的提交推送到 GitHub 遠端儲存庫。
