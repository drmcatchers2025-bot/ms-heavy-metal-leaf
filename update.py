import os
import urllib.request
import xml.etree.ElementTree as ET
from google import genai

# 1. Fetch Latest YouTube Video ID from your RSS feed
CHANNEL_ID = "UCseflqXOifRqeliqquNoYUg" 
rss_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"

try:
    req = urllib.request.urlopen(rss_url)
    xml_content = req.read()
    root = ET.fromstring(xml_content)
    ns = {'yt': 'http://www.youtube.com/xml/schemas/2015', 'atom': 'http://www.w3.org/2005/Atom'}
    latest_video = root.find('atom:entry', ns)
    video_id = latest_video.find('yt:videoId', ns).text
    embed_url = f"https://www.youtube.com/embed/{video_id}"
except Exception as e:
    print(f"Error fetching YouTube feed: {e}")
    embed_url = "https://www.youtube.com/embed/YOUR_VIDEO_ID"

# 2. Generate Daily Horoscope using Google AI Studio (Gemini)
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Act as an expert, insightful professional astrologer. Generate a concise, inspiring daily astrology reading (3 to 4 sentences) for today.",
)
horoscope_text = response.text.strip()

print("Successfully generated content from YouTube and Google AI Studio!")
