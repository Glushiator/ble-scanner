#!/usr/bin/env python3

import asyncio
import argparse
from bleak import BleakScanner, BleakError


async def scan_ble(duration: float = 5.0, sort_by_rssi: bool = False):
    """
    Scan for BLE devices for the given duration and print their addresses and advertisement data.
    
    Args:
        duration (float): Scan duration in seconds.
        sort_by_rssi (bool): If True, sort devices by RSSI (highest values first).
    """
    try:
        print(f"Scanning for {duration} seconds, please wait...")
        # Run asynchronous BLE scan; return_adv=True ensures advertisement data is included.
        devices = await BleakScanner.discover(timeout=duration, return_adv=True)
    except BleakError as e:
        print(f"BLE scanning error: {e}")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return

    if not devices:
        print("No BLE devices found.")
        return

    # Depending on the option, sort devices by RSSI (signal strength) in descending order.
    if sort_by_rssi:
        # Some devices might not have an RSSI value; treat them as very weak (-999).
        sorted_devices = sorted(
            devices.values(),
            key=lambda tup: tup[1].rssi if tup[1].rssi is not None else -999,
            reverse=True
        )
    else:
        sorted_devices = list(devices.values())

    print(f"Found {len(sorted_devices)} device(s):")
    for i, (device, adv) in enumerate(sorted_devices, start=1):
        name = device.name or "Unknown"
        addr = device.address
        rssi = adv.rssi
        print(f"{i}. {addr} ({name}), RSSI={rssi} dBm")
        
        if adv.manufacturer_data:
            # Format manufacturer data (dict of company ID -> bytes)
            mfg_items = []
            for company_id, data_bytes in adv.manufacturer_data.items():
                hex_str = data_bytes.hex()
                mfg_items.append(f"{company_id}: {hex_str}")
            print(f"    Manufacturer data: {'; '.join(mfg_items)}")
        
        if adv.service_data:
            # Format service data (dict of service UUID -> bytes)
            svc_items = []
            for uuid, data_bytes in adv.service_data.items():
                svc_items.append(f"{uuid}: {data_bytes.hex()}")
            print(f"    Service data: {'; '.join(svc_items)}")
        
        if adv.service_uuids:
            uuids = ", ".join(adv.service_uuids)
            print(f"    Service UUIDs: {uuids}")
        
        if adv.tx_power is not None:
            print(f"    TX Power: {adv.tx_power} dBm")
    # End of scanning results

def main():
    parser = argparse.ArgumentParser(
        description="Asynchronous BLE Scanner using Bleak. Optionally order devices by RSSI."
    )
    parser.add_argument(
        "--duration",
        type=float,
        default=5.0,
        help="Duration for scanning in seconds (default: 5.0)"
    )
    parser.add_argument(
        "--sort-by-rssi",
        action="store_true",
        help="Sort devices by RSSI (closest devices first)"
    )
    args = parser.parse_args()

    asyncio.run(scan_ble(duration=args.duration, sort_by_rssi=args.sort_by_rssi))

if __name__ == "__main__":
    main()
