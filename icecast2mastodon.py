import requests
import time

# Replace these values with your own
ICECAST_URL = "https://your-url/status-json.xsl"
MASTODON_TOKEN = "YOUR TOKEN"
MASTODON_URL = "https://yourdomain.com/api/v1/statuses"

def get_current_track(url):
    r = requests.get(url)
    print(r.text)
    data = r.json()
    current_track = data["icestats"]["source"]["title"]
    return current_track

def send_message(track, token, url):
    payload = {"status": f"Now playing: {track}"}
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.post(url, json=payload, headers=headers)

def main():
    last_track = ""
    while True:
        current_track = get_current_track(ICECAST_URL)
        if current_track != last_track:
            send_message(current_track, MASTODON_TOKEN, MASTODON_URL)
            last_track = current_track
        time.sleep(5)  # check every 5 seconds

if __name__ == "__main__":
    main()


