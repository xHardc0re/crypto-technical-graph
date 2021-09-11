import yfinance as yf
import plotly.graph_objs as go

data = yf.download(tickers = 'ETH-EUR', period = '30d', interval = '15m')

data['MA5'] = data['Close'].rolling(5).mean()
data['MA20'] = data['Close'].rolling(20).mean()

fig = go.Figure()
fig.add_trace(go.Candlestick(x = data.index, open = data['Open'], high = data['High'], low = data['Low'], close = data['Close'], name = 'market data'))
fig.add_trace(go.Scatter(x = data.index, y = data['MA20'], line = dict(color = 'blue', width = 1.5), name = 'Long Term MA'))
fig.add_trace(go.Scatter(x = data.index, y = data['MA5'], line = dict(color='orange', width=1.5), name = 'Short Term MA'))
fig.update_xaxes(rangeslider_visible = True, rangeselector = dict(buttons = list([dict(count = 3, label = "3d", step = "day", stepmode = "backward"), dict(count = 5, label = "5d", step = "day", stepmode = "backward"), dict(count = 7, label = "WTD", step = "day", stepmode = "todate"), dict(step = "all")])))
fig.show()
