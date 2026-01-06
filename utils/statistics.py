"""
Instance statistics and visualization utilities.

This module provides functions to analyze and display statistics
about AMP instance sets.
"""

import os
import sys
from typing import Dict, List, Any

# Add parent directory to path if running as script
if __name__ == '__main__':
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from utils.instance_loader import InstanceLoader


def analyze_instance_set(directory: str = 'instances') -> Dict[str, Any]:
    """
    Analyze all instances in the repository.
    
    Args:
        directory: Root directory containing instance folders
        
    Returns:
        Dictionary with comprehensive statistics
    """
    instances = InstanceLoader.list_instances(directory)
    
    stats = {
        'total_instances': 0,
        'by_size': {'small': 0, 'medium': 0, 'large': 0},
        'aircraft_range': {'min': float('inf'), 'max': 0},
        'tasks_range': {'min': float('inf'), 'max': 0},
        'horizon_range': {'min': float('inf'), 'max': 0},
        'aircraft_types': set(),
        'task_types': set(),
        'instances_details': []
    }
    
    for instance_type, files in instances.items():
        for filepath in files:
            instance = InstanceLoader.load_instance(filepath)
            summary = InstanceLoader.get_instance_summary(instance)
            
            stats['total_instances'] += 1
            stats['by_size'][instance_type] += 1
            
            # Update ranges
            stats['aircraft_range']['min'] = min(stats['aircraft_range']['min'], summary['num_aircraft'])
            stats['aircraft_range']['max'] = max(stats['aircraft_range']['max'], summary['num_aircraft'])
            stats['tasks_range']['min'] = min(stats['tasks_range']['min'], summary['num_tasks'])
            stats['tasks_range']['max'] = max(stats['tasks_range']['max'], summary['num_tasks'])
            stats['horizon_range']['min'] = min(stats['horizon_range']['min'], summary['planning_horizon'])
            stats['horizon_range']['max'] = max(stats['horizon_range']['max'], summary['planning_horizon'])
            
            # Collect aircraft and task types
            stats['aircraft_types'].update(summary['aircraft_by_type'].keys())
            stats['task_types'].update(summary['tasks_by_type'].keys())
            
            # Store instance details
            stats['instances_details'].append({
                'name': summary['name'],
                'type': instance_type,
                'aircraft': summary['num_aircraft'],
                'tasks': summary['num_tasks'],
                'horizon': summary['planning_horizon'],
                'hangars': summary['num_hangars'],
                'technicians': summary['total_technicians']
            })
    
    # Convert sets to sorted lists
    stats['aircraft_types'] = sorted(stats['aircraft_types'])
    stats['task_types'] = sorted(stats['task_types'])
    
    return stats


def print_statistics(stats: Dict[str, Any]) -> None:
    """
    Print formatted statistics about the instance set.
    
    Args:
        stats: Statistics dictionary from analyze_instance_set()
    """
    print("\n" + "=" * 80)
    print("AMP INSTANCE SET STATISTICS")
    print("=" * 80)
    
    print(f"\nTotal Instances: {stats['total_instances']}")
    print(f"  - Small: {stats['by_size']['small']}")
    print(f"  - Medium: {stats['by_size']['medium']}")
    print(f"  - Large: {stats['by_size']['large']}")
    
    print(f"\nAircraft Fleet Size Range: {stats['aircraft_range']['min']} - {stats['aircraft_range']['max']}")
    print(f"Maintenance Tasks Range: {stats['tasks_range']['min']} - {stats['tasks_range']['max']}")
    print(f"Planning Horizon Range: {stats['horizon_range']['min']} - {stats['horizon_range']['max']} days")
    
    print(f"\nAircraft Types: {', '.join(stats['aircraft_types'])}")
    print(f"Task Types: {', '.join(stats['task_types'])}")
    
    print("\n" + "-" * 80)
    print("INSTANCE DETAILS")
    print("-" * 80)
    print(f"{'Instance Name':<25} {'Type':<10} {'Aircraft':<10} {'Tasks':<10} {'Horizon':<10}")
    print("-" * 80)
    
    for inst in sorted(stats['instances_details'], key=lambda x: (x['type'], x['name'])):
        print(f"{inst['name']:<25} {inst['type']:<10} {inst['aircraft']:<10} "
              f"{inst['tasks']:<10} {inst['horizon']} days")
    
    print("=" * 80)


def generate_summary_table() -> str:
    """
    Generate a markdown table summarizing all instances.
    
    Returns:
        Markdown-formatted table string
    """
    instances = InstanceLoader.list_instances()
    
    lines = []
    lines.append("| Instance | Type | Aircraft | Tasks | Horizon | Hangars | Technicians |")
    lines.append("|----------|------|----------|-------|---------|---------|-------------|")
    
    for instance_type in ['small', 'medium', 'large']:
        for filepath in sorted(instances[instance_type]):
            instance = InstanceLoader.load_instance(filepath)
            summary = InstanceLoader.get_instance_summary(instance)
            
            lines.append(
                f"| {summary['name']} | {summary['type']} | "
                f"{summary['num_aircraft']} | {summary['num_tasks']} | "
                f"{summary['planning_horizon']} days | {summary['num_hangars']} | "
                f"{summary['total_technicians']} |"
            )
    
    return "\n".join(lines)


def main():
    """Generate and display instance statistics."""
    print("Analyzing AMP instance sets...")
    stats = analyze_instance_set()
    print_statistics(stats)
    
    print("\n" + "=" * 80)
    print("MARKDOWN SUMMARY TABLE")
    print("=" * 80)
    print("\n" + generate_summary_table())
    print("\n")


if __name__ == '__main__':
    main()
