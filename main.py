from sys import argv

import frida

if len(argv) < 3 or len(argv) > 3:
    exit(f"error: invalid args\nusage: python3 main.py com.package.name scripts/script.ts")

package_name = argv[1]
script_filename = argv[2]

device = frida.get_usb_device()

try:
    session = device.attach(package_name)
except:
    pid = device.spawn(package_name)
    session = device.attach(pid)
    device.resume(pid)

session.enable_jit()
script = session.create_script(open(script_filename).read().strip())
script.load()