import numpy as np
import websocket
import json
import time
from regressao import LinearRegression

# Instanciar objeto de regressão linear
regressor = LinearRegression()

# Lista para armazenar valores de y
y_vals = []

def adicionar_valor(y):
    y_vals.append(y)

    # Gerar novo valor de x a partir do comprimento da lista de valores de y
    x = np.arange(1, len(y_vals) + 1).reshape(-1, 1)

    # Treinar modelo de regressão linear com os novos valores de x e y
    regressor.fit(x, y_vals)

    # Imprimir resultados
    print(f"Coeficiente angular: {regressor.coef_}")
    print(f"Coeficiente linear: {regressor.intercept_}")
    print(f"Previsão para próximo valor de x: {regressor.predict([[len(y_vals) + 1]])}")

def on_message(ws, message):
    data = json.loads(message)
    if 'tick' in data:
        price = data['tick']['quote']
        adicionar_valor(price)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("Conexão fechada")

def on_open(ws):
    print("Conexão aberta")
    subscribe_message = {
        "ticks": "frxEURUSD",
        "subscribe": 1
    }
    ws.send(json.dumps(subscribe_message))

if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://ws.binaryws.com/websockets/v3?app_id=1089", on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.run_forever()
