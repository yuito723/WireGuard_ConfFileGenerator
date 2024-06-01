"""
WireGuard_ConfFileGenerator
(C) 2024 yuito723(https://github.com/yuito723)
"""

import subprocess as sub

a = sub.check_output("wg genkey")

print(a.decode("utf8").strip())
