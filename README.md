<img width="539" alt="Screen Shot 2023-05-04 at 10 19 20 PM" src="https://user-images.githubusercontent.com/67074258/236382876-b341ab65-4945-4997-bcf4-2dfaa6a2298d.png">

How to Request Data: 
API (GET): http://localhost:8000/filter/

Query Params = None required. 

If none are included, will return the names of all villagers in the CSV. 
Can include any combination of headers (Personality, Gender, Species, etc.). 
Can include optional param filter that will return whichever header is specified. If the header is not valid, will return all villager data the meets the other query params. For example, if the filter is "All", all villager data will be returned that meets the other query params. If the filter is "Birthday" only birthdays will be returned. The default return are Names of the villagers. 

How to Receive Data: 
The data will be returned as a list of strings unless the entire row is selected by passing in the filter parameter with the value of "All" or any string that is not a header. This will return a list of objects, each object being a row of data. 

results=[example_villager_name1, example_villager_name2, example_villager_name3, example_villager_name4, example_villager_name5, example_villager_name6]

results=[{example_villager_data}, {example_villager_data}, {example_villager_data}, {example_villager_data}, {example_villager_data}]
