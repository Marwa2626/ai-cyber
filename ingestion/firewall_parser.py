import csv
import uuid
from ingestion.schema import build_event

def parse_firewall(file_path):
    events = []

    with open(file_path, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            event_id = str(uuid.uuid4())
            timestamp = row["Time"]

            src_ip = row["Src IP"]
            action = row["Log subtype"]

            metadata = dict(row)
            metadata.pop("Time", None)

            event = build_event(
                event_id=event_id,
                timestamp=timestamp,
                source_type="firewall",
                entity_type="ip",
                entity_id=src_ip,
                event_type=f"network_{action.lower()}",
                metadata=metadata
            )

            events.append(event)

    return events
