import csv
import json
import sys
import os
from collections import defaultdict


def parse_ports(port_str):
    port_str = port_str.strip()
    if '-' in port_str:
        start, end = port_str.split('-')
        return [str(p) for p in range(int(start), int(end) + 1)]
    elif port_str:
        return [port_str]
    else:
        return []


def main():
    if len(sys.argv) < 2:
        print("Usage: python update-from-csv-file.py <path_to_csv>")
        return

    csv_path = sys.argv[1]
    if not os.path.isfile(csv_path):
        print(f"File not found: {csv_path}")
        return

    protocol_dicts = defaultdict(dict)
    processed_rows = 0

    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            print("Processing CSV table")
            for row in reader:
                port_numbers = parse_ports(row['Port Number'])
                transport_protocol = row['Transport Protocol'].lower().strip()
                service_name = row['Service Name'].strip() if row['Service Name'] else ""
                description = row['Description'].strip() if row['Description'] else "Reserved"

                # Пропуск строк без протокола
                if not transport_protocol:
                    continue

                for port_number in port_numbers:
                    if port_number in protocol_dicts[transport_protocol]:
                        if service_name and service_name not in protocol_dicts[transport_protocol][port_number]['Service Name']:
                            protocol_dicts[transport_protocol][port_number]['Service Name'] += f" / {service_name}"
                        if description and description not in protocol_dicts[transport_protocol][port_number]['Description']:
                            protocol_dicts[transport_protocol][port_number]['Description'] += f" / {description}"
                    else:
                        protocol_dicts[transport_protocol][port_number] = {
                            'Service Name': service_name,
                            'Description': description
                            }
                processed_rows += 1
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    for protocol, ports in protocol_dicts.items():
        filename = f"{protocol}.json"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(ports, f, ensure_ascii=False, indent=2)
            print(f"Saved {filename} ({len(ports)} ports)")
        except Exception as e:
            print(f"Error writing {filename}: {e}")

    print(f"Done: {processed_rows} rows processed, {len(protocol_dicts)} protocols found.")


if __name__ == '__main__':
    main()
