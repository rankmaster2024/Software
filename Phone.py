import androidhelper
import os
import socket
import time

droid = androidhelper.Android()

droid.makeToast("Scan QR to run script or connect to server")

def get_scan_text(scan):
    if not scan or not scan.result:
        return None

    r = scan.result

    if "SCAN_RESULT" in r:
        return r["SCAN_RESULT"]
    if "contents" in r:
        return r["contents"]
    if "text" in r:
        return r["text"]
    if "extras" in r and "SCAN_RESULT" in r["extras"]:
        return r["extras"]["SCAN_RESULT"]

    for k, v in r.items():
        if isinstance(v, str):
            return v
    return None


# ---------------------------
# Voice Recognition Function
# ---------------------------
def get_voice_text():
    print("\n🎤 Speak now...")
    result = droid.recognizeSpeech("Speak your command", None, None).result
    if result:
        print("You said:", result)
        return result
    else:
        print("No voice detected.")
        return ""


# ---------------------------
# Server Communication
# ---------------------------
def connect_to_server(ip, port):
    print(f"Connecting to {ip}:{port} ...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((ip, port))
        print("Connected!")
        droid.ttsSpeak("Connected to server")
        return s
    except Exception as e:
        print("Connection failed:", e)
        droid.ttsSpeak("Connection failed")
        return None


# ---------------------------
# MAIN LOOP
# ---------------------------
while True:
    scan = droid.scanBarcode()
    text = get_scan_text(scan)

    if not text:
        print("QR scan failed. Try again.")
        continue

    print("Scanned:", text)

    # ---------------------------
    # Case 1: Execute Python file
    # ---------------------------
    if text.startswith("RUN:"):
        file_path = text.replace("RUN:", "").strip()
        if os.path.exists(file_path):
            print("Running:", file_path)
            exec(open(file_path).read())
        else:
            print("File not found:", file_path)
        break

    # ---------------------------
    # Case 2: Connect to server "IP:PORT"
    # ---------------------------
    if ":" in text:
        try:
            ip, port = text.split(":")
            port = int(port)
        except:
            print("Invalid format. Expected IP:PORT")
            break

        sock = connect_to_server(ip.strip(), port)
        if not sock:
            break

        # ============================
        # Voice → Server Loop
        # ============================
        while True:
            msg = get_voice_text()
            if not msg:
                continue

            try:
                sock.send(msg.encode())
            except:
                print("Disconnected from server!")
                droid.ttsSpeak("Disconnected from server")
                break

            try:
                reply = sock.recv(4096).decode().strip()
            except:
                print("No reply from server")
                break

            print("Server:", reply)
            droid.ttsSpeak(reply)

        sock.close()
        break

    else:
        print("QR does not contain IP:PORT or RUN command.")
        break
