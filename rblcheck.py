# coding: utf8
"""
I need to test IPs in multible DNS RBLs

This script returns 1 if one or more of IPs is listed in RBLs

"""

from __future__ import print_function
import dns.resolver
import sys
BLOCKLISTS = [
    "rbl.ttk-chita.ru", "zen.spamhaus.org", "recent.spam.dnsbl.sorbs.net",
    "bl.spamcop.net"
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
                result = stub.query(query, "A")
                verbose = stub.query(query, "TXT")
                print('IP %s IS listed in %s: %s - %s' %
                      (ip2test, rbl, result[0], verbose[0]))
                any_is_listed = True
            except dns.resolver.NXDOMAIN:
                print('IP: %s is NOT listed in %s' % (ip2test, rbl))
    if any_is_listed:
        print("\nWARNING: At least one IP is listed in one or more RBLs")

    sys.exit(1 if any_is_listed else 0)

if __name__ == "__main__":
    main()
