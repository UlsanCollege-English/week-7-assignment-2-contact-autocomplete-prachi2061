import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from autocomplete_bst import BST

def build(names):
    b = BST()
    for s in names:
        b.insert(s)
    return b

# normal (4)
def test_find_and_insert():
    b = build(["amy","bob","bobby","carla"])
    assert b.find("bob") and not b.find("zara")

def test_reject_duplicates():
    b = build(["a","b"])
    assert b.insert("a") is False

def test_autocomplete_basic():
    b = build(["amy","anna","andrew","bob","bobby","carla"])
    assert b.autocomplete("an", 5) == ["andrew","anna"] or b.autocomplete("an", 5) == ["anna","andrew"]

def test_autocomplete_k_limit():
    b = build(["alice","al","ally","allen","alvin","beta"])
    out = b.autocomplete("al", 3)
    assert len(out) == 3 and all(x.startswith("al") for x in out)

# edge (3)
def test_empty_tree():
    b = BST()
    assert b.autocomplete("a", 3) == []

def test_prefix_not_present():
    b = build(["cat","dog"])
    assert b.autocomplete("z", 2) == []

def test_small_k_zero():
    b = build(["ant","ante","anthem"])
    assert b.autocomplete("an", 0) == []

# harder (3)
def test_unicode_and_case():
    b = build(["Álvaro","alfa","Al"])
    out = b.autocomplete("Al", 5)
    assert "Al" in out

def test_many_similar():
    b = build([f"app{i}" for i in range(20)])
    assert b.autocomplete("app1", 5)[:2] == ["app1","app10"]

def test_pruning_behavior_window():
    b = build(["m","n","o","p","q"])
    # ensure it doesn't wander beyond hi
    assert b.autocomplete("o", 2) == ["o","p"]
