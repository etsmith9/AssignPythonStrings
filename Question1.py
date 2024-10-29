#task 1

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

def replace_all(text, replacements):
    for replacement in replacements:
        text = text.replace(replacement, replacement.upper())
    return text

def find_keyword():
    keywords = ['good', 'excellent', 'bad', 'poor', 'average']
    new_reviews = []

    for sentence in reviews:
        new_sentence = replace_all(sentence.lower(), keywords)
        new_reviews.append(new_sentence)

    return new_reviews

updated_reviews = find_keyword()
for review in updated_reviews:
    print(review)

#task 2

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def count():
    positive_count = 0
    negative_count = 0

    for review in reviews:
        review_lower = review.lower()

        for word in positive_words:
            positive_count += review_lower.count(word)

        for word in negative_words:
            negative_count += review_lower.count(word)

    print(f"the total amount of positive words listed is: {positive_count}")
    print(f"the total amount of negative words listed is: {negative_count}")

count()

#task3 

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

def new_review(reviews):
    for review in reviews:
        
        if len(review) <= 30:
            print(review)
            continue

        summary = review[:30]

        if summary[-1] != ' ':
            last_space_index = summary.rfind(' ')
            if last_space_index != -1:
                summary = summary[:last_space_index]

        summary += "..."
        print(summary)  

new_review(reviews)
