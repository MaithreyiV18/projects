import random

def generate_random_ip():
    return f"192.168.1.{random.randint(0,20)}"

def check_firewall_rules(ip, rules):
    for rule_ip, actions in rules.items():
        if ip == rule_ip:
            return actions
    return "allow"

def main():
    firewall_rules = {
        "192.168.1.1" : "block",
        "192.168.1.4" : "block",
        "192.168.1.9" : "block",
        "192.168.1.13" : "block",
        "192.168.1.16" : "block",
        "192.168.1.19" : "block",
    }

    for _ in range(12):
        ip = generate_random_ip()
        actions = check_firewall_rules(ip, firewall_rules)
        random_number = random.randint(0,9999)
        print(f"IP: {ip}, Action: {actions}, Random, {ran>

if __name__ == "__main__":
    main()

