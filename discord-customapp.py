import os
import time

from pypresence import Presence

# A Discord application ID is public; no bot token or account password is needed.
client_id = os.environ.get("DISCORD_CLIENT_ID", "").strip()
if not client_id:
    raise RuntimeError("Set DISCORD_CLIENT_ID to your Discord application ID.")

RPC = Presence(client_id)
RPC.connect()

activity = {
    "details": "Building a project",
    "state": "Learning and experimenting",
    "start": int(time.time()),
}
RPC.update(**activity)
print("Custom activity is running. Press Ctrl+C to stop.")

try:
    while True:
        time.sleep(15)
        RPC.update(**activity)
except KeyboardInterrupt:
    pass
finally:
    RPC.close()
