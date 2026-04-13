from __future__ import annotations


def get_domain(mapping: dict) -> set:
    """Return the domain X (all inputs of the function)."""
    return set(mapping.keys())

def get_range(mapping: dict) -> set:
    return set(mapping.values())

def is_well_defined(mapping: dict, target: set) -> bool:
    return get_range(mapping).issubset(target)

def is_injective(mapping: dict) -> bool:
    return len(mapping.values()) == len(set(mapping.values()))

def is_surjective(mapping: dict, target: set) -> bool:
    return get_range(mapping) == target

def is_bijective(mapping: dict, target: set) -> bool:
    return is_injective(mapping) and is_surjective(mapping, target)