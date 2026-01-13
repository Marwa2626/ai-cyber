def build_event(event_id, timestamp, source_type, entity_type, entity_id, event_type, metadata):
    return {
        "event_id": event_id,
        "timestamp": timestamp,
        "source_type": source_type,
        "entity_type": entity_type,
        "entity_id": entity_id,
        "event_type": event_type,
        "metadata": metadata
    }
