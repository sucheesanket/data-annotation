def get_sentiment(text):
    positive_words = ["love", "good", "fantastic", "great"]
    negative_words = ["bad", "terrible", "worst"]

    text = text.lower()

    # Handle negation first
    if "not" in text:
        if any(word in text for word in positive_words):
            return "negative"
        if any(word in text for word in negative_words):
            return "positive"

    # Normal checks
    if any(word in text for word in positive_words):
        return "positive"
    elif any(word in text for word in negative_words):
        return "negative"
    else:
        return "neutral"