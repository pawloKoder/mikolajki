#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import re
import requests
import textwrap
from secrets import MAILGUN_BASE_URL, MAILGUN_API_KEY, MAILGUN_FROM
from data import DATA, SECRET_MESSAGE


def shuffle_list(some_list):
    randomized_list = some_list[:]
    while True:
        random.shuffle(randomized_list)
        for a, b in zip(some_list, randomized_list):
            if a == b:
                break
        else:
            return randomized_list


def send_mail(name, email, subject, text):
    return requests.post(MAILGUN_BASE_URL + '/messages',
        auth=("api", MAILGUN_API_KEY),
        data={"from": MAILGUN_FROM,
              "to": "{} <{}>".format(name, email),
              "subject": subject,
              "text": text})


subject_template = "Mikołajki"
message_template = "Witaj {from_name}!\n\n" +\
                   "    W wyniku losowania twoją mikołajką jest {target_name}!\n\n" +\
                   "    Twoja część sekretnej wiadomości to >>>{secret_chunk}<<< " +\
                   "wyślij ją na Facebook w celu poznania pełnej wiadomości.\n\n" +\
                   "Pozdrawiamy!"


def cipher_and_split(message, num_of_chunks):
    sm = re.sub(r"\s+", '-', message)

    chunks = map(lambda x: x.ljust(num_of_chunks, '-'), textwrap.wrap(sm, num_of_chunks))

    return map(lambda x: ''.join(x), zip(*chunks))


def do_mail():
    print "Initiating x-mass"
    people = DATA.keys()

    secret_chunks = cipher_and_split(SECRET_MESSAGE, len(DATA))
    print secret_chunks

    targets = shuffle_list(people)

    for source, target, secret_chunk in zip (people, targets, secret_chunks):
        source = DATA[source]
        target = DATA[target]

        message = message_template.format(from_name=source['full_name'],
                                          target_name=target['full_name'],
                                          secret_chunk=secret_chunk)
        send_mail(source['full_name'], source['email'], subject_template, message)

        print "Message sent to " + source['full_name']

    print "All presents are prepared!"


if __name__ == "__main__":
    do_mail()

