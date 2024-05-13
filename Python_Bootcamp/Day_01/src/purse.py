from typing import Dict


def get_ingot_count(purse: Dict[str, int]) -> int:
    if "gold_ingots" not in purse:
        return 0
    else:
        return purse["gold_ingots"]


def add_ingot(purse: Dict[str, int]) -> Dict[str, int]:
    ingots: int = get_ingot_count(purse) + 1
    new_purse = {"gold_ingots": ingots}
    return new_purse


def get_ingot(purse: Dict[str, int]) -> Dict[str, int]:
    ingots: int = 0 if get_ingot_count(purse) == 0 else purse["gold_ingots"] - 1
    new_purse = {"gold_ingots": ingots}
    return new_purse


def empty(purse: Dict[str, int]) -> Dict[str, int]:
    new_purse = {"gold_ingots": 0}
    return new_purse


if __name__ == "__main__":
    print(add_ingot(get_ingot(add_ingot(empty({})))))
