# Overcurrent Fault Block

## Overview
This block monitors current draw and triggers a fault signal when the sensed value exceeds a defined threshold. It uses a shunt resistor and comparator logic.

## Inputs
| Signal Name     | Description                          | Voltage Level |
|----------------|--------------------------------------|---------------|
| I_SENSE         | Voltage across shunt resistor         | Analog        |
| VREF_CURRENT    | Reference voltage for comparison      | Analog        |

## Outputs
| Signal Name     | Description                          | Type          |
|----------------|--------------------------------------|---------------|
| OVERCURRENT_FAULT | Fault output signal (active-high)   | Digital       |

## Logic Description
- Comparator checks if `I_SENSE > VREF_CURRENT`
- If true, `OVERCURRENT_FAULT` goes high
- Fault signal is latched externally or passed to aggregator

## Notes
- Shunt resistor value determines sensitivity
- Optional: Add low-pass filter to reduce noise

