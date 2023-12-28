#!/usr/bin/env python3

import json
import os

def convert_to_json(filepath) -> dict:
    props = {}
    with open(filepath, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            if line.startswith("#"):
                continue
            [key, value] = line.split('=', 1)
            key = key.strip()
            value = value.strip()
            props[key] = value
    return props

def main():
    dir = "props"
    data = []
    for dirpath, dirnames, filenames in os.walk(dir, topdown=True, followlinks=False):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            props = convert_to_json(filepath)
            data.append(props)

    with open("props.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False, sort_keys=True)


if __name__ == "__main__":
    main()
