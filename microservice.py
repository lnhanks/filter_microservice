import pandas as pd
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/filter/', methods=['GET'])
def filter():
    query = microservice(**request.args.to_dict())
    return query

## CSV Column Names
VALID_FILTERS = [
    "Birthday",
    "Catchphrase",
    "Color 1",
    "Color 2",
    "Favorite Song",
    "Filename",
    "Flooring",
    "Furniture List",
    "Gender",
    "Hobby",
    "Name",
    "Personality",
    "Species",
    "Style 1",
    "Style 2",
    "Unique Entry ID",
    "Wallpaper",
]

def microservice(**kwargs):
    villagers = pd.read_csv('./villagers.csv')
    if kwargs:
        query = (pd.concat([villagers[k.title()].eq(v.title()) for k, v in kwargs.items() if k.title() in VALID_FILTERS], 
                     axis=1)
           .all(axis=1))
        data = json.loads(villagers.loc[query].to_json(orient='records'))
    else:
        data = json.loads(villagers.to_json(orient='records'))
    ## Replace 'Name' with '' to return the entire row by default
    if kwargs.get('filter', 'Name').title() in VALID_FILTERS:
        data = [ row.get(kwargs.get('filter', 'Name')) for row in data ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=8000)

