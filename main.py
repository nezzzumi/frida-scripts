from sys import argv, stdin

import frida
from frida.core import Session

def on_message(message, data):
    print(message, data)


def attach_device(package_name: str) -> Session :
    device = frida.get_usb_device()
    #session = device.attach(package_name)
    pid = device.spawn(package_name)
    session = device.attach(pid)
    device.resume(pid)
    session.enable_jit()

    return session


def load_script(session: Session, script_path: str):
    script = session.create_script(open(script_path).read().strip())
    script.on("message", on_message)
    script.load()


if len(argv) < 3 or len(argv) > 3:
    exit(f"error: invalid args\nusage: python3 main.py com.package.name scripts/script.ts")

session = attach_device(argv[1])
load_script(session, argv[2])

stdin.read()