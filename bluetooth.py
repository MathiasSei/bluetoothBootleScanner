import asyncio
from bleak import BleakClient

# Replace with your bottle's address found in the scanning step
BOTTLE_ADDRESS = "71:92:CF:9B:9A:24" # Example: "A1:B2:C3:D4:E5:F6"
# Device: LARQ_1ysOqYUwlSl, Address: 71:92:CF:9B:9A:24

async def discover_services_and_characteristics(address):
    print(f"Connecting to {address}...")
    try:
        async with BleakClient(address) as client:
            if client.is_connected:
                print(f"Connected to {address}")
                for service in client.services:
                    print(f"\nService: {service.uuid} ({service.description})")
                    for char in service.characteristics:
                        print(f"  Characteristic: {char.uuid} ({char.description}) - Properties: {char.properties}")
                        if "read" in char.properties:
                            try:
                                value = await client.read_gatt_char(char.uuid)
                                print(f"    Value: {value.hex()}") # Print as hex for raw bytes
                            except Exception as e:
                                print(f"    Could not read: {e}")
            else:
                print(f"Failed to connect to {address}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(discover_services_and_characteristics(BOTTLE_ADDRESS))