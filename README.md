# AI Cybersecurity Ingestion Pipeline

This project implements a basic security telemetry ingestion and normalization pipeline.

## Data Sources
- Sysmon (Windows endpoint logs)
- Firewall logs

## Structure
- data/raw/       → raw input logs
- data/normalized → processed output
- ingestion/      → source connectors
- config/         → configuration files
- logs/           → pipeline logs
