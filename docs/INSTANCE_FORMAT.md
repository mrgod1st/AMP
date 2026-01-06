# Instance Format Specification

## Overview
This document describes the format for Aircraft Maintenance Planning (AMP) instance sets used in multi-agent reinforcement learning approaches for automated maintenance scheduling.

## Instance File Format

Instance files are provided in JSON format with the following structure:

### Root Structure
```json
{
  "instance_name": "string",
  "instance_type": "small|medium|large",
  "planning_horizon": "integer (days)",
  "aircraft_fleet": [...],
  "maintenance_tasks": [...],
  "resources": {...},
  "constraints": {...}
}
```

### Aircraft Fleet
Each aircraft in the fleet is defined with:
- `aircraft_id`: Unique identifier
- `aircraft_type`: Type/model of aircraft (e.g., "F-16", "C-130")
- `operational_status`: Current status ("operational", "maintenance", "grounded")
- `flight_hours`: Current flight hours
- `last_maintenance_date`: ISO date string
- `next_scheduled_maintenance`: Required maintenance date
- `mission_priority`: Integer (1-5, higher is more critical)

### Maintenance Tasks
Each maintenance task includes:
- `task_id`: Unique identifier
- `task_type`: Type of maintenance ("preventive", "corrective", "scheduled", "unscheduled")
- `aircraft_type`: Aircraft type this task applies to
- `duration`: Duration in hours
- `required_resources`: List of required resources
- `required_technicians`: Number and skill level required
- `deadline`: Latest completion time (ISO date)
- `priority`: Task priority (1-5)

### Resources
Resource constraints include:
- `hangars`: Number of available maintenance hangars
- `technicians`: Available technicians by skill level
- `spare_parts`: Available spare parts inventory
- `equipment`: Specialized maintenance equipment

### Constraints
Operational and scheduling constraints:
- `max_simultaneous_maintenance`: Maximum aircraft in maintenance
- `min_operational_aircraft`: Minimum operational aircraft required
- `work_shifts`: Daily work shift definitions
- `maintenance_windows`: Allowed maintenance time windows

## Instance Sizes

### Small Instances
- 5-7 aircraft
- 5-6 maintenance tasks
- 2-3 hangars
- Planning horizon: 7-14 days

### Medium Instances
- 20-25 aircraft
- 10-20 maintenance tasks
- 6-7 hangars
- Planning horizon: 30-45 days

### Large Instances
- 26+ aircraft
- 26+ maintenance tasks
- 20+ hangars
- Planning horizon: 90+ days

Note: The instance set is designed to be extensible. Researchers can create additional instances at any scale following the same format specification.

## Example Usage

See the `instances/` directory for example instance files of various sizes.
