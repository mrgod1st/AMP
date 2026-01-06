# AMP - Aircraft Maintenance Planning Instance Sets

Instance sets for **"Automated maintenance scheduling for military aircraft fleet: a multi-agent reinforcement learning approach"**

## Overview

This repository contains benchmark instance sets for the Aircraft Maintenance Planning (AMP) problem. The problem involves scheduling maintenance tasks for a fleet of military aircraft while managing limited resources and operational constraints using multi-agent reinforcement learning approaches.

## Contents

- **`instances/`**: Benchmark instance files organized by size (small, medium, large)
- **`utils/`**: Python utilities for loading, validating, and analyzing instances
- **`docs/`**: Documentation including format specifications

## Instance Sizes

- **Small**: 5-10 aircraft, 7-14 day planning horizon
- **Medium**: 20-50 aircraft, 30-60 day planning horizon  
- **Large**: 100+ aircraft, 90-180 day planning horizon

## Quick Start

### Load and validate an instance:

```python
from utils.instance_loader import InstanceLoader

# Load an instance
instance = InstanceLoader.load_instance('instances/small/instance_s1.json')

# Get summary statistics
summary = InstanceLoader.get_instance_summary(instance)
print(f"Aircraft: {summary['num_aircraft']}, Tasks: {summary['num_tasks']}")
```

### List all available instances:

```bash
python utils/instance_loader.py
```

## Problem Description

The Aircraft Maintenance Planning problem addresses:
- **Multiple aircraft types** (F-16, F-15, C-130, A-10)
- **Various maintenance tasks** (preventive, corrective, scheduled, unscheduled)
- **Resource constraints** (hangars, technicians, spare parts, equipment)
- **Operational requirements** (minimum operational aircraft, mission priorities)
- **Time constraints** (deadlines, work shifts, planning horizon)

## Documentation

- [Instance Format Specification](docs/INSTANCE_FORMAT.md)
- [Instance Set Details](instances/README.md)

## Citation

If you use these instance sets in your research, please cite:

```
@article{amp2026,
  title={Automated maintenance scheduling for military aircraft fleet: 
         a multi-agent reinforcement learning approach},
  year={2026},
  note={Instance sets available at https://github.com/mrgod1st/AMP}
}
```

## License

These instance sets are provided for research and educational purposes.
