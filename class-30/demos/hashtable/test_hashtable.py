from hashtable import Hashtable


def test_hasthtable_exists():
    hashtable = Hashtable()
    assert hashtable


def test_hash_consistency():
    hashtable = Hashtable()
    key = "apple"
    index = hashtable.hash(key)
    actual = hashtable.hash(key)
    assert actual == index


def test_same_index():
    hashtable = Hashtable()
    key_a = "listen"
    key_b = "silent"

    assert hashtable.hash(key_a) == hashtable.hash(key_b)


def test_different_index():
    hashtable = Hashtable()
    key_a = "listen"
    key_b = "zilent"

    assert hashtable.hash(key_a) != hashtable.hash(key_b)


def test_add():
    hashtable = Hashtable()
    index = hashtable.hash("spam")
    assert hashtable.buckets[index] is None
    hashtable.add("spam", "eggs")
    bucket = hashtable.buckets[index]
    assert bucket


################################################################
# STRETCH: Add with existing keys
# Danger!
# The docs and requirements don't say what to do about pre-existing keys.
# What should it do?
# What does Dictionary do?
# How might we test?
# Is it better to test now or test once get method implemented
################################################################
def test_add_same_keys():
    hashtable = Hashtable()
    hashtable.add("a", "apple")
    hashtable.add("a", "alfalfa")
    index = hashtable.hash("a")
    bucket = hashtable.buckets[index]
    assert bucket.head.value == "???"
