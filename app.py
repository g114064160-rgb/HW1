
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import warnings

# Ignore potential warnings from matplotlib for cleaner output
warnings.filterwarnings("ignore", category=UserWarning)

def main():
    """
    Main function to run the Streamlit app for simple linear regression.
    """
    st.title("互動式簡單線性回歸分析")
    st.write("這是一個使用 Streamlit 打造的互動應用程式，遵循 CRISP-DM 流程。")

    # --- Sidebar for User Inputs ---
    st.sidebar.header("數據生成參數")
    st.sidebar.write("請調整以下參數來生成新的數據集。")

    a_true = st.sidebar.slider("真實斜率 (a)", min_value=0.1, max_value=10.0, value=2.5, step=0.1)
    num_points = st.sidebar.slider("數據點數量", min_value=10, max_value=500, value=100, step=10)
    noise_level = st.sidebar.slider("雜訊等級", min_value=0.0, max_value=100.0, value=15.0, step=1.0)
    b_true = 10.0  # Keep the intercept constant for simplicity

    # --- 1. Business Understanding (商業理解) ---
    st.header("1. 商業理解 (Business Understanding)")
    st.markdown("""
    **目標**: 從一組看似隨機的數據點中，找出並量化其背後的線性關係。
    我們將建立一個簡單的線性回歸模型 (`y = ax + b`) 來預測 `y` 值。
    這個過程將模擬一個真實世界的場景，例如根據廣告支出預測銷售額。
    """)

    # --- 2. Data Understanding (資料理解) ---
    st.header("2. 資料理解 (Data Understanding)")
    st.markdown(f"""
    我們將根據您在側邊欄設定的參數來生成合成數據。
    - **真實斜率 (a)**: `{a_true}`
    - **真實截距 (b)**: `{b_true}` (固定值)
    - **數據點數量**: `{num_points}`
    - **雜訊等級**: `{noise_level}`
    """)

    # Generate data
    X = np.linspace(0, 50, num_points)
    y_true = a_true * X + b_true
    y_noisy = y_true + np.random.randn(num_points) * noise_level
    
    df = pd.DataFrame({'X': X, 'y': y_noisy})
    st.write("生成數據的前5行:")
    st.dataframe(df.head())

    # --- 3. Data Preparation (資料準備) ---
    st.header("3. 資料準備 (Data Preparation)")
    st.markdown("""
    為了讓 `scikit-learn` 函式庫能夠處理，我們需要將特徵 'X' 轉換為二維陣列。
    """ )
    
    X_train = df[['X']] # Keep it as a DataFrame (2D)
    y_train = df['y']   # Keep it as a Series (1D) 
    
    st.code(f"X 的形狀: {X_train.shape}\ny 的形狀: {y_train.shape}", language='text')
    st.success("數據已準備好用於模型訓練。")

    # --- 4. Modeling (模型建立) ---
    st.header("4. 模型建立 (Modeling)")
    st.markdown("我們將使用 `scikit-learn` 的 `LinearRegression` 來建立模型並進行訓練。" )
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    st.success("模型訓練完成！")

    # --- 5. Evaluation (模型評估) ---
    st.header("5. 模型評估 (Evaluation)")
    
    # Get model parameters
    a_pred = model.coef_[0]
    b_pred = model.intercept_
    
    st.subheader("模型評估結果:")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="原始真實斜率 (a)", value=f"{a_true:.2f}")
        st.metric(label="模型學到的斜率 (a)", value=f"{a_pred:.2f}", delta=f"{a_pred - a_true:.2f}")
    with col2:
        st.metric(label="原始真實截距 (b)", value=f"{b_true:.2f}")
        st.metric(label="模型學到的截距 (b)", value=f"{b_pred:.2f}", delta=f"{b_pred - b_true:.2f}")
    
    # Make predictions and evaluate
    y_pred = model.predict(X_train)
    mse = mean_squared_error(y_train, y_pred)
    r2 = r2_score(y_train, y_pred)
    
    st.subheader("性能指標:")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="均方誤差 (Mean Squared Error)", value=f"{mse:.2f}")
        st.info("此值越小，代表模型的預測越接近真實值。" )
    with col2:
        st.metric(label="R-squared", value=f"{r2:.2f}")
        st.info("此值越接近1，代表模型對數據的解釋能力越強。" )
    
    # Visualization
    st.subheader("視覺化結果")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(X, y_noisy, color='blue', label='原始數據 (Original Data)')
    ax.plot(X, y_pred, color='red', linewidth=2, label='擬合的迴歸線 (Fitted Line)')
    ax.plot(X, y_true, color='green', linestyle='--', linewidth=2, label='真實關係線 (True Line)')
    ax.set_title('簡單線性回歸分析')
    ax.set_xlabel('X (自變數)')
    ax.set_ylabel('y (應變數)')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    # --- 6. Deployment (部署) ---
    st.header("6. 部署 (Deployment)")
    st.markdown("""
    在這個範例中，'部署' 就是這個互動式的 Web 應用程式本身！
    您可以透過調整側邊欄的參數來即時觀察模型的變化，這對於理解線性回歸中各個參數的影響非常有幫助。
    """)

if __name__ == "__main__":
    main()
