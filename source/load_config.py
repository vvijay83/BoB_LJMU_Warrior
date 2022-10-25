import json
  
# Opening JSON file
f = open('configs.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)

# Closing file
f.close()