import pandas as pd
from binance.client import Client


def get_btc_klines(start_str, end_str=None, interval=Client.KLINE_INTERVAL_5MINUTE):
    client = Client()  # 不填API key，默认公共访问
    klines = client.get_historical_klines(
        "BTCUSDT",
        interval,
        start_str,
        end_str
    )

    df = pd.DataFrame(klines, columns=[
        "Open_time", "Open", "High", "Low", "Close", "Volume",
        "Close_time", "Quote_asset_volume", "Number_of_trades",
        "Taker_buy_base_asset_volume", "Taker_buy_quote_asset_volume", "Ignore"
    ])
    # 转换时间戳
    df["timestamps"] = pd.to_datetime(df["Open_time"], unit="ms")

    # 保留并重命名列
    df = df[["timestamps", "Open", "High", "Low", "Close", "Volume", "Quote_asset_volume"]]
    df.columns = ["timestamps", "open", "high", "low", "close", "volume", "amount"]

    # 转换为数值类型
    df[["open", "high", "low", "close", "volume", "amount"]] = df[["open", "high", "low", "close", "volume", "amount"]].astype(float)

    return df


if __name__ == "__main__":
    # 例如获取过去 3 天的 5min K线
    df = get_btc_klines("2025-8-10", None, Client.KLINE_INTERVAL_5MINUTE)

    # 保存成 CSV
    df.to_csv("BTCUSDT_5min.csv", index=False)

    print("已保存 CSV，前几行数据：")
    print(df.head())