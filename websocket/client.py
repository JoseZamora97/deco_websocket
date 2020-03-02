#!/usr/bin/env python

# WS client example
import json

import requests

from websocket.problem import Problem

url = 'http://127.0.0.1:8080/deco/api/'


def see_current_works():
    return requests.get('http://127.0.0.1:8080/works').text


def publish_work(dim=3):
    m1 = list()
    m2 = list()

    for _ in range(dim):
        row, col = Problem.generate(n=3)
        m1.append(row)
        m2.append(col)

    data = json.dumps({'m1': m1, 'm2': m2})
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    return requests.post(url + 'transaction', headers=headers, json=data).text


def get_work(amount=1):
    return requests.get(url + "get-work/" + str(amount)).text


def hello_world():
    return requests.get("http://127.0.0.1:8080/").text


if __name__ == "__main__":
    print("Hello world: ", hello_world())  # done
    print("Publish Work: ", publish_work())  # done
    print("Current Works: ", see_current_works())  # done

    # works = json.loads(get_work())
    # print("Work received: ", works)
    #
    # for w in works:
    #     Problem.operate(w)
    #
    # print(works)





