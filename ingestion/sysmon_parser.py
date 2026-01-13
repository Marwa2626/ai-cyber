import csv
import uuid
from ingestion.schema import build_event

def parse_sysmon(file_path):
    events = []

    with open(file_path, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            event_id = str(uuid.uuid4())

            # Try common Sysmon column names (your dataset may use slightly different ones)
            timestamp = row.get("UtcTime") or row.get("TimeCreated") or row.get("Time")
            computer = row.get("Computer") or row.get("Hostname") or row.get("Host")
            event_id_sysmon = row.get("EventID") or row.get("Event Id") or "unknown"

            metadata = dict(row)

            event = build_event(
                event_id=event_id,
                timestamp=timestamp,
                source_type="sysmon",
                entity_type="host",
                entity_id=computer,
                event_type=f"sysmon_event_{event_id_sysmon}",
                metadata=metadata
            )

            events.append(event)

    return events
