

#include <stdint.h>
#include <stddef.h>

// https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function
static inline uint32_t _c_fnv1a_32(const unsigned char *data, size_t len) {
    uint32_t hash = 0x811c9dc5;
    for (size_t i = 0; i < len; ++i) {
        hash = 0x01000193 * (hash ^ data[i]);
    }
    return hash;
}
