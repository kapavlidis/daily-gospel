import json
import urllib.request
from datetime import datetime
from zoneinfo import ZoneInfo

now = datetime.now(ZoneInfo("Europe/Athens"))
url = f"https://orthocal.info/api/greek/gregorian/{now.year}/{now.month}/{now.day}/"

req = urllib.request.Request(url, headers={"User-Agent": "daily-gospel-script"})
with urllib.request.urlopen(req, timeout=30) as response:
    data = json.load(response)

fast_level = data.get("fast_level_desc") or ""
fast_exception = data.get("fast_exception_desc") or ""
fasting = f"{fast_level} — {fast_exception}" if fast_exception else fast_level

gospel = data["readings"][-1]
gospel_text = " ".join(verse["content"] for verse in gospel["passage"])

message = f"{gospel['display']}\n{fasting}\n\n{gospel_text}\n"

with open("reading.txt", "w", encoding="utf-8") as f:
    f.write(message)

print(message)
