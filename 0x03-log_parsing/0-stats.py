#!/usr/bin/python3

def print_metrics(file_size, status_codes):
    """
    Print metrics
    """
    print("Total file size: {}".format(file_size))
    codes_sorted = sorted(status_codes.keys())
    for code in codes_sorted:
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


codes_count = {'200': 0, '301': 0, '400': 0, '401': 0,
               '403': 0, '404': 0, '405': 0, '500': 0}
file_size_total = 0
count = 0

try:
    while True:
        try:
            line = input()
            # Assuming line starts with IP Address, Date, etc.
            # If not, it will throw IndexError which will be handled
            status_code = line.split()[-2]
            if status_code in codes_count:
                codes_count[status_code] += 1
            # Grab file size
            file_size = int(line.split()[-1])
            file_size_total += file_size
        except (IndexError, ValueError):
            # Skip lines not in the expected format
            pass
        
        # Print metrics if 10 lines have been read
        count += 1
        if count == 10:
            print_metrics(file_size_total, codes_count)
            count = 0
except KeyboardInterrupt:
    print_metrics(file_size_total, codes_count)
    raise
