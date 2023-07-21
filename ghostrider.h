#ifndef GR_H
#define GR_H
#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>

void raptoreum_hash(const char* input, uint32_t len, char* output);

#ifdef __cplusplus
}
#endif
#endif
