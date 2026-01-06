"""
Example usage of AMP instance loader.

This script demonstrates how to load and analyze aircraft maintenance
planning instances.
"""

import sys
import os

# Add utils to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from utils.instance_loader import InstanceLoader


def main():
    """Example usage scenarios."""
    
    print("=" * 70)
    print("Aircraft Maintenance Planning - Instance Loader Example")
    print("=" * 70)
    
    # Example 1: Load a specific instance
    print("\n1. Loading a specific instance:")
    print("-" * 70)
    instance_path = 'instances/small/instance_s1.json'
    instance = InstanceLoader.load_instance(instance_path)
    print(f"✓ Successfully loaded: {instance['instance_name']}")
    print(f"  - Type: {instance['instance_type']}")
    print(f"  - Planning Horizon: {instance['planning_horizon']} days")
    print(f"  - Aircraft: {len(instance['aircraft_fleet'])}")
    print(f"  - Tasks: {len(instance['maintenance_tasks'])}")
    
    # Example 2: Get detailed summary
    print("\n2. Getting instance summary:")
    print("-" * 70)
    summary = InstanceLoader.get_instance_summary(instance)
    print(f"Instance: {summary['name']}")
    print(f"  Total Aircraft: {summary['num_aircraft']}")
    print(f"  Operational Aircraft: {summary['operational_aircraft']}")
    print(f"  Maintenance Tasks: {summary['num_tasks']}")
    print(f"  Hangars: {summary['num_hangars']}")
    print(f"  Total Technicians: {summary['total_technicians']}")
    print(f"  Aircraft by Type: {summary['aircraft_by_type']}")
    print(f"  Tasks by Type: {summary['tasks_by_type']}")
    
    # Example 3: Access specific data
    print("\n3. Accessing specific data:")
    print("-" * 70)
    print("First aircraft in fleet:")
    aircraft = instance['aircraft_fleet'][0]
    print(f"  - ID: {aircraft['aircraft_id']}")
    print(f"  - Type: {aircraft['aircraft_type']}")
    print(f"  - Status: {aircraft['operational_status']}")
    print(f"  - Flight Hours: {aircraft['flight_hours']}")
    print(f"  - Priority: {aircraft['mission_priority']}")
    
    print("\nFirst maintenance task:")
    task = instance['maintenance_tasks'][0]
    print(f"  - ID: {task['task_id']}")
    print(f"  - Type: {task['task_type']}")
    print(f"  - Aircraft: {task['aircraft_id']}")
    print(f"  - Duration: {task['duration']} hours")
    print(f"  - Deadline: {task['deadline']}")
    print(f"  - Priority: {task['priority']}")
    
    # Example 4: List all available instances
    print("\n4. Listing all available instances:")
    print("-" * 70)
    all_instances = InstanceLoader.list_instances()
    for instance_type, files in all_instances.items():
        print(f"\n{instance_type.upper()}:")
        for filepath in files:
            inst = InstanceLoader.load_instance(filepath)
            summ = InstanceLoader.get_instance_summary(inst)
            print(f"  - {os.path.basename(filepath)}: "
                  f"{summ['num_aircraft']} aircraft, "
                  f"{summ['num_tasks']} tasks, "
                  f"{summ['planning_horizon']} days")
    
    # Example 5: Validate instance structure
    print("\n5. Validating instance structure:")
    print("-" * 70)
    try:
        InstanceLoader.validate_instance(instance)
        print("✓ Instance structure is valid")
    except ValueError as e:
        print(f"✗ Validation error: {e}")
    
    print("\n" + "=" * 70)
    print("Example completed successfully!")
    print("=" * 70)


if __name__ == '__main__':
    main()
