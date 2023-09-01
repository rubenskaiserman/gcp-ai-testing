# Imports the Google Cloud client library
from google.cloud import language_v1

client = language_v1.LanguageServiceClient()

text = "I don't think you know what you're talking about what so ever. Have you even studied before started throwing out opinions?"
# text = "I love you so much"
# text = "I hate you so much I wouldn't kill you just because I want you to suffer as much as possible while you're alive"
document = language_v1.types.Document(
    content=text, type_=language_v1.types.Document.Type.PLAIN_TEXT
)

sentiment = client.analyze_sentiment(
    request={"document": document}
).document_sentiment

print(f"Text: {text}")
print(f"Sentiment: {sentiment.score}, {sentiment.magnitude}")