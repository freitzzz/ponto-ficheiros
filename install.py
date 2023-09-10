#!/usr/bin/env python3

import json
import os
from tempfile import mktemp
from typing import Any

from framework.transformer.bash import bash_module_factory
from framework.transformer.json import json_module_factory

JSON = dict[str, Any]


def find_modules():
    _modules = []

    for current_path, folders, files in os.walk('.'):
        for file in files:
            if file.endswith('.json'):
                _json = json.load(open(os.path.join(current_path, file)))
                if _json.get('definitions') is None:
                    _modules.append(_json)

    return _modules


modules = find_modules()

modules = json_module_factory.create_multiple(modules)
scripts = bash_module_factory.create_multiple(modules)

for script in scripts:
    # print(script)
    # continue
    temp = mktemp()

    file = open(temp, "w+")
    file.write(script)
    file.close()

    os.system(f"cat {temp} | bash")