import requests,json

payload = json.dump({
    'age':12,
    'sex':'F'
})

response = requests.put('http://127.0.0.1:8000/predict',data=payload)

print(response.json)