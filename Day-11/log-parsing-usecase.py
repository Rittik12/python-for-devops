def find_unique_ip(file_path):
    unique_ips = set()
    with open(file_path, "r") as file:
        for line in file:
            parts = line.split()
            if len(parts) < 7:
                continue

            ip, status_code = parts[2], parts[5]
            if status_code.isdigit() and 500 <= int(status_code) <=599:
                    unique_ips.add(ip)
    return (unique_ips)

ips=find_unique_ip("E:\\python-for-devops\python-for-devops\Day-11\log-file.log")
print(f"ipcount: {len(ips)}, list of ips:{(ips)}" )



                
