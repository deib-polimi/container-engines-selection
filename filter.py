import json
import time
import csv
import sys

types = ['cloud', 'iot', 'hpc']
tags = {
    'cloud' : {'cloud', 'container'},
    'iot' : {'iot', 'internet of things', 'container'},
    'hpc' : {'hpc', 'high performance computing', 'container'}
}

output = open('dataset.csv', 'w')
writer = csv.writer(output)
keywords = ['full_name', 'stargazers_count', 'description', 'html_url']
writer.writerow([*keywords, 'type'])

for type in types:
    with open(f'github-results/{type}.json', 'r') as fj:
        data = json.load(fj)
        items = data['items']
        for item in items:
            desc = item['description']
            if not desc:
                continue
            desc = desc.replace("-", " ").lower()
            for tag in tags[type]:
                if tag in desc:
                    repo = [item[k] for k in keywords]
                    writer.writerow([*repo, type])
                    break

output.close()