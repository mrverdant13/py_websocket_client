from websocket import create_connection


def send_and_wait_for_response(
    ws_url: str = 'ws://echo.websocket.org',
    msg: str = 'Hello, world!!!!!',
):
    """Single echo.
    
    Open a WS connection with `ws_url`, send `msg`, wait for `msg` return and close connection.

    Args:
        ws_url (str, optional): WS URL to connect with. Defaults to 'ws://echo.websocket.org'.
        msg (str, optional): Message to be sent and received back. Defaults to 'Hello, world!!!!!'.
    """
    print()
    ws = create_connection(ws_url)
    print('Sending "{}"...'.format(msg))
    ws.send(msg)
    print("Sent!")
    print()
    print("Waiting for message return...")
    msg = ws.recv()
    print('Received "{}"'.format(msg))
    ws.close()
