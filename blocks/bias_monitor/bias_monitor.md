# Bias Monitor Block

## Overview
This block senses the amplifier bias voltage and outputs a scaled analog signal (`BIAS_VSENSE`) for fault detection. It typically uses a resistor divider and optional filtering.

## Inputs
| Signal Name     | Description                     | Voltage Level |
|----------------|----------------------------------|---------------|
| BIAS_RAW        | Raw bias voltage from amplifier  | Analog        |

## Outputs
| Signal Name     | Description                     | Type          |
|----------------|----------------------------------|---------------|
| BIAS_VSENSE     | Scaled bias voltage              | Analog        |

## Logic Description
- Voltage divider scales `BIAS_RAW` to safe range for comparator input
- Optional RC filter smooths noise
- Output feeds into `bias_fault` block

## Notes
- Divider ratio should match expected bias range (e.g. 60V → 5V)
- Use precision resistors for accurate sensing
- Place close to bias source to minimize noise pickup
