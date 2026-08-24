from flask import Flask
import requests

app = Flask(__name__)

servers = [
    "http://cloudcity.local:5001",
    "http://cloudcity.local:5002"
]

current_server = 0


def get_healthy_servers():
    healthy_servers = []

    for server in servers:
        try:
            response = requests.get(server, timeout=2)

            if response.status_code == 200:
                healthy_servers.append(server)

        except requests.RequestException:
            pass

    return healthy_servers


@app.route("/")
def load_balance():
    global current_server

    healthy_servers = get_healthy_servers()

    if not healthy_servers:
        return "No healthy servers available", 503

    # Select the next healthy server using round robin
    server = healthy_servers[current_server % len(healthy_servers)]

    current_server += 1

    response = requests.get(server, timeout=2)

    return response.text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)