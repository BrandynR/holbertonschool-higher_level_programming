#!/usr/bin/python3
"""
script that takes in a string and sends a search request to the Star Wars API
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get('https://swapi.co/api/people', params={'search': argv[1]})
    ppl = r.json()
    print("Number of results: {}".format(ppl.get('count')))
    for person in ppl.get('results'):
        print(person.get('name'))
