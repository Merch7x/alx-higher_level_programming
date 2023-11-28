#!/usr/bin/python3
string = []


def magic_string():
    string.append("bet")
    return ("BestSchool, " * len(string)).removesuffix(", ")
