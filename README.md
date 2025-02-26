# BLE Scanner Utility with Bleak

This repository contains a Python-based BLE scanner utility that leverages the [Bleak](https://github.com/hbldh/bleak) library to perform Bluetooth Low Energy (BLE) scans. The utility is designed to scan for nearby BLE devices asynchronously and print their addresses along with relevant advertisement data. An option is provided to sort devices by RSSI, so you can easily see the closest devices first.

## Features

- **Asynchronous Scanning:** Utilizes Python's `asyncio` to perform BLE scanning without blocking.
- **Comprehensive Advertisement Data:** Retrieves and prints advertisement details including:
  - Device Address and Name
  - RSSI (signal strength)
  - Manufacturer Data
  - Service Data and Service UUIDs
  - TX Power (if available)
- **Command-Line Options:**
  - Set scan duration (`--duration`).
  - Sort devices by RSSI (`--sort-by-rssi`).
- **Modern BLE Interface:** Built using the Bleak library, ensuring compatibility with contemporary BLE hardware and operating systems.

## Requirements

- Python 3.7 or later
- [Bleak](https://github.com/hbldh/bleak) library

## Installation

1. **Clone the Repository:**

       git clone https://github.com/yourusername/ble-scanner-bleak.git
       cd ble-scanner-bleak

2. **Install Dependencies:**

   It is recommended to use a virtual environment:

       python3 -m venv venv
       source venv/bin/activate  # On Windows, use venv\Scripts\activate
       pip install -r requirements.txt

   If a `requirements.txt` is not present, install Bleak directly:

       pip install bleak

## Usage

Run the scanner with default options:

       python scanner.py

### Command-Line Options

- **Scan Duration:**  
  Specify the duration of the scan (in seconds) using the `--duration` option.

       python scanner.py --duration 10.0

- **Sort by RSSI:**  
  Use the `--sort-by-rssi` flag to display the closest devices first based on RSSI.

       python scanner.py --sort-by-rssi

- **Combine Options:**  
  You can combine both options as needed:

       python scanner.py --duration 10.0 --sort-by-rssi

## How It Works

1. **Scanning:**  
   The scanner uses `BleakScanner.discover()` to search for BLE devices over a specified duration. This function returns both the device objects and their advertisement data.

2. **Processing Results:**  
   Once the scan is complete, the script sorts the results by RSSI (if specified) and prints each device’s details in a user-friendly format.

3. **Output:**  
   The output includes device address, name, RSSI, and additional advertisement information, which can be useful for debugging, development, or simply monitoring nearby BLE devices.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/ble-scanner-bleak/issues).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The original C BLE scanner utility by David G. Young and Damian Kołakowski served as inspiration for this project.
- Thanks to the [Bleak](https://github.com/hbldh/bleak) community for their excellent work on the library.

---

Enjoy scanning BLE devices with this utility, and happy coding!
