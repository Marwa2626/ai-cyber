import json
from ingestion.firewall_parser import parse_firewall
from ingestion.sysmon_parser import parse_sysmon

def main():
    firewall_events = parse_firewall("data/raw/firewall/firewall.csv")
    sysmon_events = parse_sysmon("data/raw/sysmon/sysmon.csv")

    all_events = firewall_events + sysmon_events

    print(f"Loaded {len(firewall_events)} firewall events")
    print(f"Loaded {len(sysmon_events)} sysmon events")

    with open("data/normalized/events.json", "w", encoding="utf-8") as f:
        json.dump(all_events, f, indent=2)

    print("Saved normalized events to data/normalized/events.json")

if __name__ == "__main__":
    main()
