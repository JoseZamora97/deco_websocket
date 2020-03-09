#!/usr/bin/env python

# WS client example
import json

import requests

from websocket.problem import Problem
from websocket.sign_keys import Security

url = 'http://127.0.0.1:8081/deco/api/'


def see_current_works():
    return requests.get('http://127.0.0.1:8081/works').text


def get_fee() -> int:
    return 100


def get_from():
    return Security.load_key_pairs()


def get_nonce():
    return 10
    # return json.loads(requests.get(url + '/getNonce').text)['nonce']


def publish_work(dim=1):
    m1 = list()
    m2 = list()

    for _ in range(dim):
        row, col = Problem.generate(n=1)
        m1.append(row)
        m2.append(col)

    keys = get_from()

    fee = get_fee()
    from_ = str(keys['public'])
    nonce = get_nonce()

    to_sign = str(keys['public']) + str(nonce)
    signature = str(Security.get_signature(to_sign.encode('utf-8')))

    data = json.dumps({
        'm1': m1,
        'm2': m2,
        'fee': fee,
        'from': from_,
        'nonce': nonce,
        'signature': signature
    })

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    return requests.post(url + 'transaction', headers=headers, json=data).text


def get_work(amount=2):
    return requests.get(url + "get-work/" + str(amount)).text


def hello_world():
    return requests.get("http://127.0.0.1:8081/").text


if __name__ == "__main__":

    Security.generate()

    print("Hello world: ", hello_world())  # done
    print("Publish Work: ", publish_work())  # done
    # print("Current Works: ", see_current_works())  # done

    # works = json.loads(get_work())
    # print("Work received: \n", works)



