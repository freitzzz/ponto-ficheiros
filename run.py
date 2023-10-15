#!/usr/bin/env python3
from framework.core.const import installed_modules_path
from framework.core.log import put_snakes_to_work, ConsoleLumberSnakeClient
from framework.installer.installer import Installer
from framework.transformer.bash import bash_module_factory
from framework.transformer.json import json_module_factory, json_profile_factory

put_snakes_to_work(
    [
        ConsoleLumberSnakeClient()
    ]
)

installer = Installer(
    installed_modules_directory=installed_modules_path,
    modules_directory=".",
    profile_path="profiles/personal.json",
    _json_module_factory=json_module_factory,
    _bash_module_factory=bash_module_factory,
    _json_profile_factory=json_profile_factory,

)

installer.run()
