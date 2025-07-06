## 🇷🇺  [Русская версия](./README_EN.md)

# TCP/UDP Port Dictionary

This project provides a tool to convert a CSV file from [http://www.iana.org](https://www.iana.org/assignments/service-names-port-numbers) with port and protocol information into separate JSON files for each protocol (e.g., `tcp.json`, `udp.json`). Each JSON file contains a dictionary where the key is the port number and the value is an object with the service name and description.

## Features

- Parses single ports and port ranges (e.g., `80`, `272-279`).
- Handles missing protocol, service name, or description fields.
- Outputs one JSON file per protocol.

## Usage

1. Place your CSV file (e.g., `service-names-port-numbers.csv`) in the project directory.
2. Run the script:

   ```bash
   python update-from-csv-file.py service-names-port-numbers.csv
   ```

3. The script will generate files like `tcp.json`, `udp.json`, etc.

## Output Format

Each JSON file has the following structure:

```json
{
  "80": {
    "Service Name": "http",
    "Description": "World Wide Web HTTP"
  },
  "272": {
    "Service Name": "",
    "Description": "Unassigned"
  }
}
```

## Requirements

- Python 3.x
