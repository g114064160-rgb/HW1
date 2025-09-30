# CRISP-DM 流程總結 (process_summary.md)

本專案遵循 CRISP-DM (Cross-Industry Standard Process for Data Mining) 方法論，將簡單線性回歸的分析過程分為以下階段：

## 1. 商業理解 (Business Understanding)
**目標**: 從一組看似隨機的數據點中，找出並量化其背後的線性關係。我們將建立一個簡單的線性回歸模型 (`y = ax + b`) 來預測 `y` 值。這個過程將模擬一個真實世界的場景，例如根據廣告支出預測銷售額。

## 2. 資料理解 (Data Understanding)
我們根據使用者在側邊欄設定的參數來生成合成數據，包括：
- **真實斜率 (a)**
- **真實截距 (b)** (固定值)
- **數據點數量**
- **雜訊等級**

## 3. 資料準備 (Data Preparation)
為了讓 `scikit-learn` 函式庫能夠處理，我們需要將特徵 'X' 轉換為二維陣列。數據已準備好用於模型訓練。

## 4. 模型建立 (Modeling)
使用 `scikit-learn` 的 `LinearRegression` 來建立模型並進行訓練。

## 5. 模型評估 (Evaluation)
- **模型參數**: 獲取模型學到的斜率 (a_pred) 和截距 (b_pred)，並與真實值進行比較。
- **性能指標**: 計算均方誤差 (Mean Squared Error, MSE) 和 R-squared 值來評估模型性能。
- **視覺化**: 繪製原始數據、擬合的迴歸線和真實關係線，直觀展示模型效果。

## 6. 部署 (Deployment)
在這個範例中，'部署' 就是這個互動式的 Web 應用程式本身！使用者可以透過調整側邊欄的參數來即時觀察模型的變化，這對於理解線性回歸中各個參數的影響非常有幫助。
