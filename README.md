# 互動式簡單線性回歸分析

這是一個使用 Streamlit 框架開發的互動式應用程式，旨在展示簡單線性回歸的整個流程，並遵循 CRISP-DM (Cross-Industry Standard Process for Data Mining) 方法論。

## 專案目標
- 透過互動式介面，讓使用者能夠調整數據生成參數，即時觀察線性回歸模型的建立、訓練和評估過程。
- 模擬數據科學專案的典型階段：商業理解、資料理解、資料準備、模型建立、模型評估和部署。

## 功能特色
- **數據生成**: 使用者可以調整真實斜率、數據點數量和雜訊等級來生成合成數據。
- **CRISP-DM 流程**: 應用程式結構清晰，對應 CRISP-DM 的六個階段。
- **模型訓練與評估**: 使用 `scikit-learn` 訓練線性回歸模型，並顯示模型的斜率、截距、均方誤差 (MSE) 和 R-squared 值。
- **視覺化**: 透過 `matplotlib` 繪製原始數據、真實關係線和模型擬合的迴歸線，直觀展示模型效果。

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
本應用程式可以輕鬆部署到 Streamlit Cloud 或其他支援 Streamlit 的平台。

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
