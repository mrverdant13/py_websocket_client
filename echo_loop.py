import websocket
from typing import Callable
try:
    import thread
except ImportError:
    import _thread as thread
import time


def on_message(
    ws: websocket._app.WebSocketApp,
    msg: str,
):
    print('Received "{}"'.format(msg))


def on_error(
    ws: websocket._app.WebSocketApp,
    error,
):
    print(error)


def on_close(ws: websocket._app.WebSocketApp):
    print("WS connection closed!!!")


def on_open(ws: websocket._app.WebSocketApp):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send("Hello {}".format(i))
        time.sleep(1)
        print("Closing WS connection...")
        ws.close()

    thread.start_new_thread(run, ())


if __name__ == "__main__":
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        "ws://echo.websocket.org/",
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )
    ws.on_open = on_open
    ws.run_forever()