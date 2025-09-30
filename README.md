# 互動式簡單線性回歸分析

這是一個使用 Streamlit 框架開發的互動式應用程式，旨在展示簡單線性回歸的整個流程，並遵循 CRISP-DM (Cross-Industry Standard Process for Data Mining) 方法論。

## 專案目標
- 透過互動式介面，讓使用者能夠調整數據生成參數，即時觀察線性回歸模型的建立、訓練和評估過程。
- 模擬數據科學專案的典型階段：商業理解、資料理解、資料準備、模型建立、模型評估和部署。

## 功能特色
- **數據生成**: 使用者可以調整真實斜率、數據點數量和雜訊等級來生成合成數據。
- **模型訓練與評估**: 使用 `scikit-learn` 訓練線性回歸模型，並顯示模型的斜率、截距、均方誤差 (MSE) 和 R-squared 值。
- **視覺化**: 透過 `matplotlib` 繪製原始數據、真實關係線和模型擬合的迴歸線，直觀展示模型效果。

## CRISP-DM 流程概述
本專案遵循 CRISP-DM (Cross-Industry Standard Process for Data Mining) 方法論，將簡單線性回歸的分析過程分為以下階段：

1.  **商業理解 (Business Understanding)**: 旨在從數據中找出並量化線性關係，建立預測模型。
2.  **資料理解 (Data Understanding)**: 根據使用者設定的參數生成合成數據，理解數據特性。
3.  **資料準備 (Data Preparation)**: 將數據轉換為模型可處理的格式，例如將特徵轉換為二維陣列。
4.  **模型建立 (Modeling)**: 使用 `scikit-learn` 的 `LinearRegression` 建立並訓練模型。
5.  **模型評估 (Evaluation)**: 評估模型性能，包括模型參數、均方誤差 (MSE) 和 R-squared 值，並透過視覺化展示結果。
6.  **部署 (Deployment)**: 本應用程式本身即為部署形式，提供互動式介面供使用者探索模型。

## 如何運行 (本地)

1.  **克隆儲存庫**:
    ```bash
    git clone https://github.com/g114064160-rgb/HW1.git
    cd HW1
    ```

2.  **安裝依賴**:
    請確保您已安裝 Python。然後，安裝所有必要的函式庫：
    ```bash
    pip install -r requirements.txt
    ```
    或者手動安裝：
    ```bash
    pip install streamlit scikit-learn pandas matplotlib numpy
    ```

3.  **運行應用程式**:
    在專案根目錄下，執行以下命令：
    ```bash
    python -m streamlit run app.py
    ```
    這將在您的預設網頁瀏覽器中打開 Streamlit 應用程式。

## 部署
本應用程式已部署至 Streamlit Cloud，您可以透過以下連結訪問：
[Streamlit App Link](https://hbs7fn5b5cernetj3okpvp.streamlit.app/)

您也可以將本應用程式輕鬆部署到其他支援 Streamlit 的平台。

## 檔案結構
- `app.py`: Streamlit 應用程式的主要程式碼。
- `simple_linear_regression.py`: (如果有的話，此處可描述其功能)
- `README.md`: 專案說明文件。
- `requirements.txt`: Python 依賴列表。
- `log.md`: 專案開發日誌。
- `process_summary.md`: CRISP-DM 流程總結。
- `steps.md`: 專案執行步驟記錄。

## 貢獻
歡迎提出問題或貢獻程式碼。

## 許可
[請在此處填寫您的許可資訊，例如 MIT License]
