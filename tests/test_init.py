from fnvhash import fnv1a_32 as fnvhash_fnv1a_32

from fnv_hash_fast import fnv1a_32


def test_fnv1a_32():
    assert fnv1a_32(b"") == 2166136261  # FNV1a_32 offset basis
    assert fnv1a_32(b"hello") == 1335831723
    assert fnv1a_32(b"goodbye") == 1188507472
    assert fnv1a_32(b"goodbye" * 4096) == 386067909


def test_fnvhash_fnv1a_32():
    for test_data in (
        b"",
        b"hello",
        b"goodbye",
        b"goodbye" * 4096,
    ):
        assert fnv1a_32(test_data) == fnvhash_fnv1a_32(test_data)


def test_ha_compat_hash_fnvhash():
    assert (
        fnvhash_fnv1a_32(
            b'{"action":"update","entity_id":"update.twizzy_software_update","changes":{"entity_category":"diagnostic","supported_features":4}}'
        )
        == 1724124935
    )
    assert (
        fnvhash_fnv1a_32(
            b'{"domain":"input_text","service":"set_value","service_data":{"value":1680573390.26158,"entity_id":["input_text.last_motion_in_house"]}}'
        )
        == 2209002508
    )


def test_ha_compat_hash():
    assert (
        fnv1a_32(
            b'{"action":"update","entity_id":"update.twizzy_software_update","changes":{"entity_category":"diagnostic","supported_features":4}}'
        )
        == 1724124935
    )
    assert (
        fnv1a_32(
            b'{"domain":"input_text","service":"set_value","service_data":{"value":1680573390.26158,"entity_id":["input_text.last_motion_in_house"]}}'
        )
        == 2209002508
    )
