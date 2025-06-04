import asyncio
from bleak import BleakScanner

async def scan_for_devices():
    print("Scanning for Bluetooth devices...")
    devices = await BleakScanner.discover(timeout=5.0) # Scan for 5 seconds

    for device in devices:
        print(f"Device: {device.name}, Address: {device.address}")
        # You might also want to print device.details for more info
        # print(f"  Details: {device.details}")

if __name__ == "__main__":
    asyncio.run(scan_for_devices())