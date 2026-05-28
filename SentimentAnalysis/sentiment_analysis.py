import requests
import json

def sentiment_analyzer(text_to_analyse):
    url = "https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"
    headers = {
        "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"
        }
    payload = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code==200:
        formatted_response = json.loads(response.text)
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif response.status_code==500:
        label = None 
        score = None
        print(f"{response.status_code}")
    else:
        label = None 
        score = None
        print(f"{response.status_code}")
    return {"label":label, "score":score}

    

