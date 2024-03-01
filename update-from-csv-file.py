import csv
import json


def main():
    result_dict = {}
    processed_rows = 0
    cvss_path = r""

    with open(cvss_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        print("Processing CVS table")
        for row in reader:
            port_number = row['Port Number']
            transport_protocol = row['Transport Protocol']
            service_name = row['Service Name']
            description = row['Description']
            if transport_protocol == 'tcp':
                if port_number in result_dict:
                    if service_name not in result_dict[port_number]:
                        result_dict[port_number]['Service Name'] += f" / {service_name}"
                    if description not in result_dict[port_number]:
                        result_dict[port_number]['Description'] += f" / {description}"
                    print(port_number, " ", result_dict[port_number])

                else:
                    result_dict[port_number] = {'Service Name': service_name,
                                                'Description': description}
                    print(port_number, " ", result_dict[port_number])
            processed_rows += 1

    with open("port-desc.txt", "w") as f:
        f.write(f"port_dict = {json.dumps(result_dict)}")

    print(f"Done : {processed_rows} rows processed : {len(result_dict)} Ports in dict")
    print("Saved to port-desc.txt")


if __name__ == '__main__':
    main()
