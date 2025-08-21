# Fault Latch Block

## Overview
This block captures and holds fault signals until a reset command is received. It ensures that transient faults are latched and visible for diagnostics or system response.

## Inputs
| Signal Name       | Description                          | Type    |
|-------------------|--------------------------------------|---------|
| FAULT_IN          | Incoming fault signal                | Digital |
| RESET_LATCH       | Active-high reset signal             | Digital |

## Outputs
| Signal Name       | Description                          | Type    |
|-------------------|--------------------------------------|---------|
| FAULT_LATCHED     | Latched fault output                 | Digital |

## Logic Description
- On rising edge of `FAULT_IN`, `FAULT_LATCHED` goes high
- `FAULT_LATCHED` remains high until `RESET_LATCH` is asserted
- Optional: Add LED indicator or MCU interrupt output

## Notes
- Use SR latch or D flip-flop with asynchronous reset
- Consider debounce on `RESET_LATCH` if manual
