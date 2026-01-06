"""
Instance loader and validator for Aircraft Maintenance Planning (AMP) instances.

This module provides utilities to load, validate, and parse instance files
for the aircraft maintenance scheduling problem.
"""

import json
import os
from typing import Dict, List, Optional, Any
from datetime import datetime


class InstanceLoader:
    """Load and validate AMP instance files."""
    
    VALID_INSTANCE_TYPES = ['small', 'medium', 'large']
    VALID_STATUSES = ['operational', 'maintenance', 'grounded']
    VALID_TASK_TYPES = ['preventive', 'corrective', 'scheduled', 'unscheduled']
    VALID_SKILL_LEVELS = ['expert', 'intermediate', 'novice']
    
    @staticmethod
    def load_instance(filepath: str) -> Dict[str, Any]:
        """
        Load an instance from a JSON file.
        
        Args:
            filepath: Path to the instance JSON file
            
        Returns:
            Dictionary containing the instance data
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            json.JSONDecodeError: If the file is not valid JSON
            ValueError: If the instance format is invalid
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Instance file not found: {filepath}")
        
        with open(filepath, 'r') as f:
            instance = json.load(f)
        
        InstanceLoader.validate_instance(instance)
        return instance
    
    @staticmethod
    def validate_instance(instance: Dict[str, Any]) -> None:
        """
        Validate instance structure and data.
        
        Args:
            instance: Instance dictionary to validate
            
        Raises:
            ValueError: If validation fails
        """
        # Check required top-level fields
        required_fields = ['instance_name', 'instance_type', 'planning_horizon',
                          'aircraft_fleet', 'maintenance_tasks', 'resources', 'constraints']
        
        for field in required_fields:
            if field not in instance:
                raise ValueError(f"Missing required field: {field}")
        
        # Validate instance type
        if instance['instance_type'] not in InstanceLoader.VALID_INSTANCE_TYPES:
            raise ValueError(f"Invalid instance_type: {instance['instance_type']}")
        
        # Validate planning horizon
        if not isinstance(instance['planning_horizon'], int) or instance['planning_horizon'] <= 0:
            raise ValueError(f"planning_horizon must be a positive integer")
        
        # Validate aircraft fleet
        InstanceLoader._validate_aircraft_fleet(instance['aircraft_fleet'])
        
        # Validate maintenance tasks
        InstanceLoader._validate_maintenance_tasks(instance['maintenance_tasks'])
        
        # Validate resources
        InstanceLoader._validate_resources(instance['resources'])
        
        # Validate constraints
        InstanceLoader._validate_constraints(instance['constraints'])
    
    @staticmethod
    def _validate_aircraft_fleet(fleet: List[Dict[str, Any]]) -> None:
        """Validate aircraft fleet data."""
        if not isinstance(fleet, list) or len(fleet) == 0:
            raise ValueError("aircraft_fleet must be a non-empty list")
        
        aircraft_ids = set()
        for aircraft in fleet:
            required_fields = ['aircraft_id', 'aircraft_type', 'operational_status',
                             'flight_hours', 'last_maintenance_date', 
                             'next_scheduled_maintenance', 'mission_priority']
            
            for field in required_fields:
                if field not in aircraft:
                    raise ValueError(f"Aircraft missing required field: {field}")
            
            # Check for duplicate IDs
            if aircraft['aircraft_id'] in aircraft_ids:
                raise ValueError(f"Duplicate aircraft_id: {aircraft['aircraft_id']}")
            aircraft_ids.add(aircraft['aircraft_id'])
            
            # Validate status
            if aircraft['operational_status'] not in InstanceLoader.VALID_STATUSES:
                raise ValueError(f"Invalid operational_status: {aircraft['operational_status']}")
            
            # Validate priority
            if not (1 <= aircraft['mission_priority'] <= 5):
                raise ValueError(f"mission_priority must be between 1 and 5")
    
    @staticmethod
    def _validate_maintenance_tasks(tasks: List[Dict[str, Any]]) -> None:
        """Validate maintenance tasks data."""
        if not isinstance(tasks, list):
            raise ValueError("maintenance_tasks must be a list")
        
        task_ids = set()
        for task in tasks:
            required_fields = ['task_id', 'task_type', 'aircraft_id', 'aircraft_type',
                             'duration', 'required_resources', 'required_technicians',
                             'deadline', 'priority']
            
            for field in required_fields:
                if field not in task:
                    raise ValueError(f"Task missing required field: {field}")
            
            # Check for duplicate IDs
            if task['task_id'] in task_ids:
                raise ValueError(f"Duplicate task_id: {task['task_id']}")
            task_ids.add(task['task_id'])
            
            # Validate task type
            if task['task_type'] not in InstanceLoader.VALID_TASK_TYPES:
                raise ValueError(f"Invalid task_type: {task['task_type']}")
            
            # Validate priority
            if not (1 <= task['priority'] <= 5):
                raise ValueError(f"Task priority must be between 1 and 5")
            
            # Validate technicians
            for tech in task['required_technicians']:
                if tech['skill_level'] not in InstanceLoader.VALID_SKILL_LEVELS:
                    raise ValueError(f"Invalid skill_level: {tech['skill_level']}")
    
    @staticmethod
    def _validate_resources(resources: Dict[str, Any]) -> None:
        """Validate resources data."""
        required_sections = ['hangars', 'technicians', 'spare_parts', 'equipment']
        
        for section in required_sections:
            if section not in resources:
                raise ValueError(f"Resources missing required section: {section}")
        
        # Validate hangars
        if 'total' not in resources['hangars']:
            raise ValueError("Hangars must have 'total' field")
        
        # Validate technicians
        for skill in InstanceLoader.VALID_SKILL_LEVELS:
            if skill not in resources['technicians']:
                raise ValueError(f"Technicians missing skill level: {skill}")
    
    @staticmethod
    def _validate_constraints(constraints: Dict[str, Any]) -> None:
        """Validate constraints data."""
        required_fields = ['max_simultaneous_maintenance', 'min_operational_aircraft',
                          'work_shifts', 'maintenance_windows']
        
        for field in required_fields:
            if field not in constraints:
                raise ValueError(f"Constraints missing required field: {field}")
        
        # Validate work shifts
        if not isinstance(constraints['work_shifts'], list):
            raise ValueError("work_shifts must be a list")
        
        for shift in constraints['work_shifts']:
            if 'shift_name' not in shift or 'start_hour' not in shift or 'end_hour' not in shift:
                raise ValueError("Each work shift must have shift_name, start_hour, and end_hour")
    
    @staticmethod
    def list_instances(directory: str = 'instances') -> Dict[str, List[str]]:
        """
        List all available instances by type.
        
        Args:
            directory: Root directory containing instance folders
            
        Returns:
            Dictionary mapping instance types to lists of file paths
        """
        instances = {'small': [], 'medium': [], 'large': []}
        
        for instance_type in instances.keys():
            type_dir = os.path.join(directory, instance_type)
            if os.path.exists(type_dir):
                for filename in os.listdir(type_dir):
                    if filename.endswith('.json'):
                        instances[instance_type].append(
                            os.path.join(type_dir, filename)
                        )
        
        return instances
    
    @staticmethod
    def get_instance_summary(instance: Dict[str, Any]) -> Dict[str, Any]:
        """
        Get a summary of an instance.
        
        Args:
            instance: Instance dictionary
            
        Returns:
            Dictionary with summary statistics
        """
        summary = {
            'name': instance['instance_name'],
            'type': instance['instance_type'],
            'planning_horizon': instance['planning_horizon'],
            'num_aircraft': len(instance['aircraft_fleet']),
            'num_tasks': len(instance['maintenance_tasks']),
            'num_hangars': instance['resources']['hangars']['total'],
            'total_technicians': sum(instance['resources']['technicians'].values()),
            'aircraft_by_type': {},
            'tasks_by_type': {},
            'operational_aircraft': 0,
        }
        
        # Count aircraft by type
        for aircraft in instance['aircraft_fleet']:
            aircraft_type = aircraft['aircraft_type']
            summary['aircraft_by_type'][aircraft_type] = \
                summary['aircraft_by_type'].get(aircraft_type, 0) + 1
            
            if aircraft['operational_status'] == 'operational':
                summary['operational_aircraft'] += 1
        
        # Count tasks by type
        for task in instance['maintenance_tasks']:
            task_type = task['task_type']
            summary['tasks_by_type'][task_type] = \
                summary['tasks_by_type'].get(task_type, 0) + 1
        
        return summary


def main():
    """Example usage of the InstanceLoader."""
    # List all available instances
    instances = InstanceLoader.list_instances()
    
    print("Available Instances:")
    print("-" * 50)
    for instance_type, files in instances.items():
        print(f"\n{instance_type.upper()} instances: {len(files)}")
        for filepath in files:
            print(f"  - {os.path.basename(filepath)}")
    
    print("\n" + "=" * 50)
    print("Instance Summaries:")
    print("=" * 50)
    
    # Load and summarize each instance
    for instance_type, files in instances.items():
        for filepath in files:
            try:
                instance = InstanceLoader.load_instance(filepath)
                summary = InstanceLoader.get_instance_summary(instance)
                
                print(f"\n{summary['name']} ({summary['type']})")
                print(f"  Planning horizon: {summary['planning_horizon']} days")
                print(f"  Aircraft: {summary['num_aircraft']} total, {summary['operational_aircraft']} operational")
                print(f"  Maintenance tasks: {summary['num_tasks']}")
                print(f"  Hangars: {summary['num_hangars']}")
                print(f"  Technicians: {summary['total_technicians']}")
                print(f"  Aircraft types: {', '.join(f'{k}({v})' for k, v in summary['aircraft_by_type'].items())}")
                print(f"  Task types: {', '.join(f'{k}({v})' for k, v in summary['tasks_by_type'].items())}")
                
            except Exception as e:
                print(f"\nError loading {filepath}: {e}")


if __name__ == '__main__':
    main()
