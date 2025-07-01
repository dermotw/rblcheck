#!/usr/bin/env python3
# coding: utf8
"""
I need to test IPs in multible DNS RBLs

This script returns 1 if one or more of IPs is listed in RBLs

"""

from __future__ import print_function
import dns.resolver
import sys
BLOCKLISTS = [
        "b.barracudacentral.org",
        "sbl-xbl.spamhaus.org",
        "pbl.spamhaus.org",
        "zen.spamhaus.org",
        "black.junkemailfilter.com",
        "psbl.surriel.com",
        "hil.habeas.com",
        "bl.nordspam.com",
        "bogons.cymru.com",
        "dyna.spamrats.com",
        "spam.spamrats.com",
        "ubl.unsubscore.com"
]


def main():
    """
    Test IPs from command line
    """
    if len(sys.argv) == 1:
        print("Usage: %s ip1 [ip2 [ip3...]]" % sys.argv[0])
        sys.exit(2)

    stub = dns.resolver.Resolver()
    any_is_listed = False
    for ip2test in sys.argv[1:]:
        for rbl in BLOCKLISTS:
            try:
                query = '.'.join(reversed(str(ip2test).split("."))) + "." + rbl
                result = stub.resolve(query, "A")
                print('IP %s IS listed in %s: %s' %
                      (ip2test, rbl, result[0]))
                any_is_listed = True
            except dns.resolver.NXDOMAIN:
                pass

    sys.exit(1 if any_is_listed else 0)

if __name__ == "__main__":
    main()
