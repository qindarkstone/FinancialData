import akshare as ak
import pandas as pd

# 选择10只股票，例如
stocks = ["sh600000", "sh600036", "sh601398", "sz000002", "sz000651",
          "sz002415", "sz002475", "sz300015", "sz300059", "sz300760"]

# 定义最大涨幅和最大跌幅变量
max_increase = 0
max_decrease = 0
max_increase_stock = ""
max_decrease_stock = ""


all_data = pd.DataFrame()
# 用循环遍历10只股票，并逐个获取数据
for stock in stocks:
    print(f"正在下载 {stock} 的数据...")
    data = ak.stock_zh_a_daily(symbol=stock, adjust="hfq")
    # 将数据保存到CSV文件
    data.to_csv(f"{stock}.csv", index=False)

    # 统计涨幅和跌幅
    increase = (data.iloc[-1]["close"] - data.iloc[0]["close"]) / data.iloc[0]["close"]
    decrease = (data.iloc[-1]["close"] - data.iloc[0]["close"]) / data.iloc[-1]["close"]

    # 判断是否为最大涨幅和最大跌幅
    if increase > max_increase:
        max_increase = increase
        max_increase_stock = stock
    if decrease < max_decrease:
        max_decrease = decrease
        max_decrease_stock = stock

all_data.to_csv("all_stocks_data.csv", index=False)
# 输出最大涨幅和最大跌幅的股票代码和涨幅/跌幅值
print(f"涨幅最大的股票是：{max_increase_stock}，涨幅为：{max_increase:.2%}")
print(f"跌幅最大的股票是：{max_decrease_stock}，跌幅为：{max_decrease:.2%}")
print("数据下载完成！")

