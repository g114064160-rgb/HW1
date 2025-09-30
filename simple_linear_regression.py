
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import warnings

# Ignore potential warnings from matplotlib for cleaner output
warnings.filterwarnings("ignore", category=UserWarning)

def run_linear_regression_process():
    """
    Main function to run the CRISP-DM process for simple linear regression.
    """
    
    # --- 1. Business Understanding (商業理解) ---
    print("="*60)
    print("1. CRISP-DM Step: Business Understanding (商業理解)")
    print("="*60)
    print("目標: 我們的目標是從一組看似隨機的數據點中，找出並量化其背後的線性關係。")
    print("      我們將建立一個簡單的線性回歸模型 (y = ax + b) 來預測 y 值。")
    print("      這個過程將模擬一個真實世界的場景，例如根據廣告支出預測銷售額。")
    print("\n")

    # --- 2. Data Understanding (資料理解) ---
    print("="*60)
    print("2. CRISP-DM Step: Data Understanding (資料理解)")
    print("="*60)
    print("我們將生成一些合成數據來模擬真實世界的數據。")
    print("您可以自定義數據的特性。")

    # Get user input for data generation
    try:
        a_true = float(input("請輸入真實的斜率 'a' (例如 2.5): ") or 2.5)
        num_points = int(input("請輸入要生成的數據點數量 (例如 100): ") or 100)
        noise_level = float(input("請輸入雜訊等級 (例如 15.0): ") or 15.0)
    except ValueError:
        print("輸入無效，將使用預設值。")
        a_true = 2.5
        num_points = 100
        noise_level = 15.0

    b_true = 10.0  # We'll keep the intercept constant for simplicity
    
    print(f"\n數據生成參數: a={a_true}, b={b_true}, 數量={num_points}, 雜訊={noise_level}")

    # Generate data
    X = np.linspace(0, 50, num_points)
    y_true = a_true * X + b_true
    y_noisy = y_true + np.random.randn(num_points) * noise_level
    
    df = pd.DataFrame({'X': X, 'y': y_noisy})
    print("\n生成數據的前5行:")
    print(df.head())
    print("\n")

    # --- 3. Data Preparation (資料準備) ---
    print("="*60)
    print("3. CRISP-DM Step: Data Preparation (資料準備)")
    print("="*60)
    print("為了讓 scikit-learn 函式庫能夠處理，我們需要將特徵 'X' 轉換為二維陣列。")
    
    X_train = df[['X']] # Keep it as a DataFrame (2D)
    y_train = df['y']   # Keep it as a Series (1D)
    
    print(f"X 的形狀: {X_train.shape}")
    print(f"y 的形狀: {y_train.shape}")
    print("數據已準備好用於模型訓練。")
    print("\n")

    # --- 4. Modeling (模型建立) ---
    print("="*60)
    print("4. CRISP-DM Step: Modeling (模型建立)")
    print("="*60)
    print("我們將使用 scikit-learn 的 LinearRegression 來建立模型。")
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    print("模型訓練完成！")
    print("\n")

    # --- 5. Evaluation (模型評估) ---
    print("="*60)
    print("5. CRISP-DM Step: Evaluation (模型評估)")
    print("="*60)
    
    # Get model parameters
    a_pred = model.coef_[0]
    b_pred = model.intercept_
    
    print("模型評估結果:")
    print(f"  - 原始真實斜率 (a): {a_true:.2f}")
    print(f"  - 模型學到的斜率 (a): {a_pred:.2f}")
    print(f"  - 原始真實截距 (b): {b_true:.2f}")
    print(f"  - 模型學到的截距 (b): {b_pred:.2f}")
    
    # Make predictions and evaluate
    y_pred = model.predict(X_train)
    mse = mean_squared_error(y_train, y_pred)
    r2 = r2_score(y_train, y_pred)
    
    print("\n性能指標:")
    print(f"  - 均方誤差 (Mean Squared Error): {mse:.2f}")
    print("    (此值越小，代表模型的預測越接近真實值)")
    print(f"  - R-squared: {r2:.2f}")
    print("    (此值越接近1，代表模型對數據的解釋能力越強)")
    
    # Visualization
    print("\n正在生成結果圖表...")
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y_noisy, color='blue', label='原始數據 (Original Data)')
    plt.plot(X, y_pred, color='red', linewidth=2, label='擬合的迴歸線 (Fitted Line)')
    plt.plot(X, y_true, color='green', linestyle='--', linewidth=2, label='真實關係線 (True Line)')
    plt.title('簡單線性回歸分析')
    plt.xlabel('X (自變數)')
    plt.ylabel('y (應變數)')
    plt.legend()
    plt.grid(True)
    plt.show()
    print("\n")

    # --- 6. Deployment (部署) ---
    print("="*60)
    print("6. CRISP-DM Step: Deployment (部署)")
    print("="*60)
    print("在這個範例中，'部署' 就是這個可執行的腳本。")
    print("您可以重複執行此腳本，嘗試不同的參數組合來觀察模型的變化。")
    print("下一步可以將此邏輯轉移到 Streamlit 或 Flask 等 Web 框架中，創建一個互動式的 Web 應用程式。")
    print("="*60)

if __name__ == "__main__":
    run_linear_regression_process()
