import json
import websocket
import time
import requests

# Static values
BROWSER_ID_KEY = "6335bf8b-7294-5d8e-8bbc-75cb2b0fdfe3"
PERMISSIONS_KEY = True
extension_id = "ilehaonighjijnmpnagapkhpcdbhclfg"
USER_ID_KEY = "e5ace647-0cb8-46f8-9d47-19abd6d72b1c"
version = "5.0.0"

director_server = "https://director.getgrass.io"
RECONNECT_INTERVAL = 0.5  # 500ms
PING_INTERVAL = 120  # 2 minutes
token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJseGtPeW9QaWIwMlNzUlpGeHBaN2JlSzJOSEJBMSJ9.eyJ1c2VySWQiOiJlNWFjZTY0Ny0wY2I4LTQ2ZjgtOWQ0Ny0xOWFiZDZkNzJiMWMiLCJlbWFpbCI6ImpyYy5qYXkzOEBnbWFpbC5jb20iLCJzY29wZSI6IlNFTExFUiIsImlhdCI6MTczNjY5NDA4NSwibmJmIjoxNzM2Njk0MDg1LCJleHAiOjE3Njc3OTgwODUsImF1ZCI6Ind5bmQtdXNlcnMiLCJpc3MiOiJodHRwczovL3d5bmQuczMuYW1hem9uYXdzLmNvbS9wdWJsaWMifQ.XSsSLwNy5_IRDRXHndYzwsIPKh5fRK4bxZmALPvf5TYPAVESxAK9mlirRvtO0Uj9Xp4FMMv5vHW-vTOLH2Lp55vzyGvNyM-fpcGlc7aCPIpMgvAemnc_qDchQfUFmLkdBSA1zzMQvwhy_ID-8lzZZXnlC5lzHDZUvKR_aBBldZGiJAjpOivQZSwZzrRTgIxg-K5PtQ2y-l0pamSN9iDqD89-Mh_Q_ApiHEcstME0Iglpt0ks7nCNhpRn67tPVy25QiYgIGRUvQmxd3eq2bySvOO6BtOGodL4jep8s4QmbnbJRQfnProAC_GBrpVztbMy3VyDRXLvptnQqWWlirCRgA"

def get_unix_timestamp():
    return int(time.time())

def checkin():
    """Fetches destinations from the director server."""
    try:
        headers = {"Content-Type": "application/json"}
        payload = {
            "browserId": BROWSER_ID_KEY,
            "userId": USER_ID_KEY,
            "version": version,
            "extensionId": extension_id,
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
            "deviceType": "extension"
        }
        response = requests.post(f"{director_server}/checkin", json=payload, headers=headers)
        data = response.json()
        destinations = data.get("destinations", [])
        tokenData = data.get("token", "")
        return destinations[0], tokenData
    except Exception as e:
        print("Checkin failed:", e)
        return []

def on_message(ws, message):
    print("Received message:", message)
    try:
        data = json.loads(message)
        response = {
            "id": data.get("id"),
            "origin_action": data.get("action"),
            "result": "Success"
        }
        ws.send(json.dumps(response))
    except json.JSONDecodeError:
        print("Error: Invalid JSON received")

def on_error(ws, error):
    print("Error:", error)

def on_close(ws, close_status_code, close_msg):
    print(f"WebSocket closed. Code: {close_status_code}, Reason: {close_msg}")

def on_open(ws):
    print("WebSocket connected!")
    ws.send(json.dumps({"action": "checkin", "version": version}))

def connect_websocket():
    destinations, tokenData = checkin()
    if not destinations:
        print("No destinations received. Retrying...")
        time.sleep(RECONNECT_INTERVAL)
        return connect_websocket()

    print("Received destinations:", destinations)
    if not destinations:
        print("No destinations received. Retrying...")
        time.sleep(RECONNECT_INTERVAL)
        return connect_websocket()


    ws_url = f"ws://{destinations}?token={token}"
    print(f"Trying to connect to: {ws_url}")

    try:
        ws = websocket.WebSocketApp(
            ws_url,
            on_message=on_message,
            on_error=on_error,
            on_close=on_close
        )
        ws.on_open = on_open
        ws.run_forever()
    except Exception as e:
        print(f"WebSocket connection failed for {ws_url}: {e}")
    
    time.sleep(RECONNECT_INTERVAL)  # Wait before trying next destination

if __name__ == "__main__":
    connect_websocket()
