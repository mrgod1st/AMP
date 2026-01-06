# Aircraft Maintenance Planning (AMP) Instance Sets

This directory contains benchmark instance sets for the **Automated Maintenance Scheduling for Military Aircraft Fleet** problem using multi-agent reinforcement learning approaches.

## Overview

The Aircraft Maintenance Planning (AMP) problem involves scheduling maintenance tasks for a fleet of military aircraft while considering:
- Multiple aircraft types with different maintenance requirements
- Various maintenance task types (preventive, corrective, scheduled, unscheduled)
- Limited resources (hangars, technicians, spare parts, equipment)
- Operational constraints (minimum operational aircraft, work shifts, deadlines)
- Mission priorities and urgency levels

## Instance Structure

Each instance is provided in JSON format with the following components:

### 1. Aircraft Fleet
- Aircraft identification and type
- Current operational status
- Flight hours and maintenance history
- Scheduled maintenance requirements
- Mission priority levels (1-5)

### 2. Maintenance Tasks
- Task identification and type
- Required duration and resources
- Technician requirements by skill level
- Deadlines and priority levels
- Aircraft-task associations

### 3. Resources
- **Hangars**: Available maintenance facilities with capacity constraints
- **Technicians**: Available personnel by skill level (expert, intermediate, novice)
- **Spare Parts**: Inventory of replacement components
- **Equipment**: Specialized maintenance tools and systems

### 4. Constraints
- Maximum simultaneous maintenance operations
- Minimum operational aircraft requirements
- Work shift schedules
- Maintenance windows (weekdays, weekends, holidays)

## Instance Sizes

### Small Instances (`instances/small/`)
- **Aircraft**: 5-7 aircraft
- **Tasks**: 5-6 maintenance tasks
- **Hangars**: 2-3 facilities
- **Planning Horizon**: 7-14 days
- **Use Case**: Algorithm development, quick testing, parameter tuning

Example instances:
- `instance_s1.json`: 5 aircraft (F-16, C-130), 5 tasks, 14-day horizon
- `instance_s2.json`: 7 aircraft (A-10, F-15), 5 tasks, 10-day horizon
- `instance_s3.json`: 6 aircraft (F-16, C-130), 6 tasks, 7-day horizon

### Medium Instances (`instances/medium/`)
- **Aircraft**: 20-25 aircraft
- **Tasks**: 10-20 maintenance tasks
- **Hangars**: 6-7 facilities
- **Planning Horizon**: 30-45 days
- **Use Case**: Realistic testing, performance evaluation, comparison studies

Example instances:
- `instance_m1.json`: 25 aircraft (F-16, F-15, C-130, A-10), 10 tasks, 30-day horizon
- `instance_m2.json`: 20 aircraft (F-16, F-15, C-130, A-10), 20 tasks, 45-day horizon

### Large Instances (`instances/large/`)
- **Aircraft**: 26+ aircraft
- **Tasks**: 26+ maintenance tasks
- **Hangars**: 20+ facilities
- **Planning Horizon**: 90+ days
- **Use Case**: Scalability testing, extended planning scenarios, computational challenge

Example instances:
- `instance_l1.json`: 26 aircraft (F-16, F-15, C-130, A-10), 26 tasks, 90-day horizon

Note: The large instance category is designed to be extensible. Additional larger instances can be created following the same format for more challenging scalability tests.

## Aircraft Types

The instances include various military aircraft types:
- **F-16 Fighting Falcon**: Multirole fighter aircraft
- **F-15 Eagle**: Air superiority fighter
- **C-130 Hercules**: Transport aircraft
- **A-10 Thunderbolt II**: Close air support aircraft

Each aircraft type has different:
- Maintenance requirements and durations
- Hangar space requirements
- Technician skill level requirements
- Operational priorities

## Maintenance Task Types

1. **Preventive**: Scheduled maintenance to prevent failures
2. **Corrective**: Repair of identified issues
3. **Scheduled**: Routine periodic maintenance
4. **Unscheduled**: Emergency or urgent repairs

## Resource Constraints

### Technician Skill Levels
- **Expert**: Highly skilled, can handle complex tasks
- **Intermediate**: Standard maintenance capabilities
- **Novice**: Basic maintenance support

### Equipment Types
- Engine tools and diagnostic equipment
- Avionics and radar systems
- Hydraulic equipment
- Electrical tools
- Weapons systems
- Structural repair tools

## Usage

### Loading Instances with Python

```python
from utils.instance_loader import InstanceLoader

# Load a specific instance
instance = InstanceLoader.load_instance('instances/small/instance_s1.json')

# Get instance summary
summary = InstanceLoader.get_instance_summary(instance)
print(f"Instance: {summary['name']}")
print(f"Aircraft: {summary['num_aircraft']}")
print(f"Tasks: {summary['num_tasks']}")

# List all available instances
instances = InstanceLoader.list_instances()
for instance_type, files in instances.items():
    print(f"{instance_type}: {len(files)} instances")
```

### Running the Instance Loader

```bash
cd /path/to/AMP
python utils/instance_loader.py
```

This will display a summary of all available instances.

## Instance Format Specification

See [`docs/INSTANCE_FORMAT.md`](../docs/INSTANCE_FORMAT.md) for detailed format specification and schema.

## Validation

All instances are validated against the following criteria:
- Correct JSON structure
- Required fields present
- Valid data types and ranges
- Consistent aircraft and task references
- Resource feasibility
- Constraint compatibility

Use the `InstanceLoader.validate_instance()` method to validate custom instances.

## Creating Custom Instances

To create custom instances:
1. Follow the format specification in `docs/INSTANCE_FORMAT.md`
2. Use existing instances as templates
3. Validate using `InstanceLoader.load_instance()`
4. Place in the appropriate size category folder

## Citation

If you use these instance sets in your research, please cite:

```
@article{amp2026,
  title={Automated maintenance scheduling for military aircraft fleet: a multi-agent reinforcement learning approach},
  year={2026},
  note={Instance sets available at https://github.com/mrgod1st/AMP}
}
```

## Problem Characteristics

- **Decision Variables**: Task scheduling times, resource assignments
- **Objectives**: Minimize downtime, meet deadlines, balance workload
- **Constraints**: Resource capacity, precedence, simultaneity
- **Complexity**: NP-hard combinatorial optimization problem
- **Approach**: Multi-agent reinforcement learning

## Benchmark Results

Future releases will include baseline performance metrics for:
- Greedy heuristics
- Priority-based scheduling
- Multi-agent RL approaches
- Hybrid optimization methods

## Contributing

Contributions of additional instances are welcome! Please ensure:
- Instances follow the format specification
- Instances validate successfully
- Realistic and diverse scenarios
- Clear documentation of instance characteristics

## License

These instance sets are provided for research and educational purposes.
