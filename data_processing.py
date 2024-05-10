import pandas as pd

def build_schema(df):
    datetime = []
    mix_pd = []
    buy_signal = []
    sell_signal = []
    signal1 = []
    for i in df:
        lst = i.translate(str.maketrans({'[': '', ']': '', '$': ''})).split(' ')

        datetime.append(lst[0])
        mix_pd.append(lst[3])
        buy_signal.append(lst[4])
        sell_signal.append(lst[5])
        signal1.append(lst[13])

    output = pd.DataFrame({
        'datetime': datetime,
        'mix_pd': mix_pd,
        'buy_signal': buy_signal,
        'sell_signal': sell_signal,
        'signal1': signal1
    })
    return output

def smooth_data(df, window_size=10):
    df['mid_px_smooth'] = df['mix_pd'].rolling(window=window_size).mean()
    df['buy_signal_smooth'] = df['buy_signal'].rolling(window=window_size).mean()
    df['sell_signal_smooth'] = df['sell_signal'].rolling(window=window_size).mean()
    return df
