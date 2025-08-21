# Thermal Fault Block

## Overview
This block monitors system temperature and triggers a fault signal when the sensed value exceeds a defined threshold. It uses a thermistor voltage divider and comparator logic.

## Inputs
| Signal Name     | Description                          | Voltage Level |
|----------------|--------------------------------------|---------------|
| THERM_VSENSE    | Voltage from thermistor divider       | Analog        |
| VREF_THERM      | Reference voltage for comparison      | Analog        |

## Outputs
| Signal Name     | Description                          | Type          |
|----------------|--------------------------------------|---------------|
| THERMAL_FAULT   | Fault output signal (active-high)     | Digital       |

## Logic Description
- Comparator checks if `THERM_VSENSE < VREF_THERM`
- If true, `THERMAL_FAULT` goes high
- Fault signal is latched externally

## Notes
- Thermistor type and divider values determine threshold
- Add hysteresis to avoid false triggering

