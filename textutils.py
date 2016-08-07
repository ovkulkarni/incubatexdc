import indicoio
import os

indicoio.config.api_key = os.getenv("INDICO_API_KEY", "")

def analyze(text):
	val = indicoio.sentiment(text)
	if val < 0.2:
		return "bad"
	elif val < 0.4:
		return "warning"
	else:
		return "good"