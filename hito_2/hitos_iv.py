#!/usr/bin/env python
"""Modulo de funciones para manejar el archivo JSON de los hitos."""

import json


def read_json(json_file='hitos.json'):
    """Devuelve un diccionario con el archivo JSON."""
    milestone_dict = {}
    try:
        with open(json_file, 'r') as f:
            milestone_dict = json.loads(f.read())
    except Exception as e:
        raise
    finally:
        return milestone_dict


def milestone_number(milestone_dict):
    """Carga JSON file into a dictionary."""
    return len(milestone_dict['hitos'])


if __name__ == '__main__':
    milestones = read_json()
    print(
        json.dumps(
            milestones, sort_keys=True, indent=2, separators=(',', ' : ')))
    print('Milestone number: ', milestone_number(milestones))
