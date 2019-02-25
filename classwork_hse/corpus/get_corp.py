import urllib.request
import json
from token_key import k

url = "https://api.vk.com/method/wall.get?owner_id=81595441&count=2&v=5.7&access_token=" + k

content = urllib.request.urlopen(url)
decoded_content = content.read().decode("utf-8")
data = json.loads(decoded_content)
print(data)