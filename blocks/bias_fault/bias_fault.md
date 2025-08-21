# Bias Fault Block

## Overview
This block monitors bias voltage levels and triggers a fault signal if they fall outside the safe operating range.

## Inputs
| Signal Name     | Description                     | Voltage Level |
|----------------|----------------------------------|---------------|
| BIAS_MON        | Bias voltage monitor input       | Analog        |
| VREF_BIAS       | Reference voltage for comparison | Analog        |

## Outputs
| Signal Name     | Description                     | Type          |
|----------------|----------------------------------|---------------|
| BIAS_FAULT      | Fault output signal              | Digital (Active High) |

## Logic Description
- Comparator checks if `BIAS_MON` < `VREF_BIAS - margin`
- If true, `BIAS_FAULT` goes high
- Fault signal is latched externally

## Notes
- Add hysteresis to avoid false triggering
- Document threshold margin in schematic

