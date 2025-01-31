# Predict sentiment using BERT  
from transformers import pipeline  

classifier = pipeline("sentiment-analysis")  
result = classifier("I love AI!")  
print(result)  # Output: [{'label': 'POSITIVE', 'score': 0.99}]  
