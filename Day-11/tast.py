def count_error_ips(filepath="E:\python-for-devops\python-for-devops\Day-11\log-file.log"):
    """Count unique IPs that hit a 5xx server error."""
    error_ips = set() 

    with open(filepath, "r") as f:
        for line in f:
            parts = line.split()
            if len(parts) < 7:
                continue  # skip malformed/blank lines

            ip, status = parts[2], parts[5]
            if status.isdigit() and 500 <= int(status) <= 599:
                error_ips.add(ip)

    return len(error_ips)


if __name__ == "__main__":
    print(count_error_ips("E:\python-for-devops\python-for-devops\Day-11\log-file.log"))