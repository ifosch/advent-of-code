#!/usr/bin/env python

from pprint import pprint
from aocd import AocdError

import re

try:
    from aocd import data, submit
except AocdError:
    exit("Something is not right (probably missing day)")


def A():

    passport = {}
    valid = 0
    for line in data.splitlines():
        if line:
            for i in line.split():
                k, v = i.split(":")
                passport[k] = v
            continue

        if hasallfields(passport):
            valid += 1
        
        passport = {}

    else:
        if hasallfields(passport):
            valid += 1

    return valid


def B():
    passport = {}
    valid = 0
    for line in data.splitlines():
        if line:
            for i in line.split():
                k, v = i.split(":")
                passport[k] = v
            continue

        if hasallfields(passport) and isvalid(passport):
            valid += 1
        
        passport = {}

    else:
        if hasallfields(passport) and isvalid(passport):
            valid += 1

    return valid


def isvalid(passport):
    for k, v in passport.items():
        if k == 'byr':
            if not len(v) == 4:
                return False
            if int(v) < 1920 or int(v) > 2002:
                return False
        elif k == 'iyr':
            if not len(v) == 4:
                return False
            if int(v) < 2010 or int(v) > 2020:
                return False
        elif k == 'eyr':
            if not len(v) == 4:
                return False
            if int(v) < 2020 or int(v) > 2030:
                return False
        elif k == 'hgt':
            if v.endswith('in'):
                h = int(v[:-2])
                if h < 59 or h > 76:
                    return False
            elif v.endswith('cm'):
                h = int(v[:-2])
                if h < 150 or h > 193:
                    return False
            else:
                return False
        elif k == "hcl":
            if not re.match(r"^#[0-9a-f]{6}$", v):
                return False
        elif k == "ecl":
            if v not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                return False
        elif k == "pid":
            if not re.match(r"^[0-9]{9}$", v):
                return False

    return True


def hasallfields(passport):
    fields = (
        'byr',  # (Birth Year)
        'iyr',  # (Issue Year)
        'eyr',  # (Expiration Year)
        'hgt',  # (Height)
        'hcl',  # (Hair Color)
        'ecl',  # (Eye Color)
        'pid',  # (Passport ID)
        'cid',  # (Country ID)
    )

    for f in fields:
        if f == 'cid':
            continue

        if f not in passport:
            return False

    return True


def print_solutions():
    for part in ['A', 'B']:
        print("PART {}:".format(part), globals()[part]())


if __name__ == "__main__":
    print_solutions()
