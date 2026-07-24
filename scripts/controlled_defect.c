/*
 * TACTIC Task 01: controlled target-specific build defect.
 * Expected:
 *   ESP32    -> FAIL
 *   ESP32-S3 -> PASS
 */
#include "sdkconfig.h"

#if defined(CONFIG_IDF_TARGET_ESP32) && CONFIG_IDF_TARGET_ESP32
#error "TACTIC_TASK_01: controlled ESP32-only build failure"
#endif
