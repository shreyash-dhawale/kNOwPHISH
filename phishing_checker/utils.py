import requests
from django.conf import settings

def detect_phishing(url):
    safe_browsing_api_url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={settings.GOOGLE_SAFE_BROWSING_API_KEY}"
    payload = {
        "client": {
            "clientId": "yourcompanyname",
            "clientVersion": "1.5.2"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "POTENTIALLY_HARMFUL_APPLICATION"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [
                {"url": url}
            ]
        }
    }

    response = requests.post(safe_browsing_api_url, json=payload)
    if response.status_code == 200:
        data = response.json()
        if 'matches' in data:
            return True  # Phishing URL
        else:
            return False  # Safe URL
    else:
        return None  # Error analyzing URL
