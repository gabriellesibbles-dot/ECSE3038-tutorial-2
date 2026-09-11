readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]
def list_devices(devices):
    for device in devices:
        print(f"{device['name']} ({device['room']}) - {device['temp']}°C - {'Online' if device['online'] else 'Offline'}")

list_devices(readings),


def average_temp(devices):
    if not devices:
        return 0
    return sum(device["temp"] for device in devices) / len(devices)

print(f"Average temperature: {average_temp(readings):.2f}°C")

def hottest(devices):
    if not devices:
        return None
    return max(devices, key=lambda device: device["temp"])


print(hottest(readings))


def to_status(device):
    return {
        "device": device["name"],
        "status": "Online" if device["online"] else "Offline",
        "celsius": device["temp"],
    }


print(to_status(readings[0]))


def by_room(devices):
    rooms = {}
    for device in devices:
        rooms.setdefault(device["room"], []).append(device["name"])
    return rooms


print(by_room(readings))




