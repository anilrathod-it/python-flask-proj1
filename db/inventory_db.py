db = {
  "items": [
    {
      "name": "Item1",
      "vendor": "V1",
      "model": "M1",
      "location": "India",
    },
    {
      "name": "Item2",
      "vendor": "V2",
      "model": "M2",
      "location": "USA",
    },
    {
      "name": "Item3",
      "vendor": "V3",
      "model": "M3",
      "location": "UK",
    }, 
    {
      "name": "Item4",
      "vendor": "V4",
      "model": "M4",
      "location": "Germany",
    }
  ]
}

def get_inventory():
	global db
	return db['items']