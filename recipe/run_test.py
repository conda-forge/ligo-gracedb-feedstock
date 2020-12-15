#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2020 Cardiff University <macleoddm@cardiff.ac.uk>

import warnings

from requests import RequestException

from ligo.gracedb.rest import GraceDb


def test_superevents():
    """Basic functionality test of ligo-gracedb

    Connect to the default server, and print the IDs of the first
    10 superevents with a FAR < 1e9

    Notes
    -----
    The whole function needs to be protected against a RequestException
    because there is no network activity until the first superevent
    is pulled out of the ``<events>`` generator.
    """
    conn = GraceDb(
        force_noauth=True,
    )
    events = conn.superevents(
        "far<1e9",
        columns=[
            "superevent_id",
            "gw_id",
        ],
    )
    for i, event in enumerate(events):
        if i >= 10:  # stop after 10
            break
        print(
            event["superevent_id"],
            event["gw_id"],
        )


if __name__ == "__main__":
    try:
        test_superevents()
    except RequestException as exc:
        # if the connection failed, we don't care, but we do care
        # about any other failure
        warnings.warn(
            "caught {}: {}".format(type(exc).__name__, str(exc)),
        )
