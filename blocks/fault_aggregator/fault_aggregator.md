# Fault Aggregator Block

## Overview
This block consolidates fault signals from multiple subsystems (bias, thermal, overcurrent, relay) into a single fault output. It uses OR logic to flag any active fault and optionally encodes fault sources for diagnostics.

## Inputs
| Signal Name        | Description                          | Type    |
|--------------------|--------------------------------------|---------|
| BIAS_FAULT         | Bias voltage fault                   | Digital |
| THERMAL_FAULT      | Thermal threshold fault              | Digital |
| OVERCURRENT_FAULT  | Overcurrent fault                    | Digital |
| RELAY_FAULT        | Relay mismatch fault                 | Digital |

## Outputs
| Signal Name        | Description                          | Type    |
|--------------------|--------------------------------------|---------|
| FAULT_GLOBAL       | Aggregated fault signal              | Digital |
| FAULT_CODE[3:0]    | Optional encoded fault source        | Digital |

## Logic Description
- `FAULT_GLOBAL = BIAS_FAULT OR THERMAL_FAULT OR OVERCURRENT_FAULT OR RELAY_FAULT`
- Optional: Use priority encoder to generate `FAULT_CODE` for diagnostics
- Fault signal can be latched or reset externally

## Notes
- Consider adding fault masking or override inputs
- Useful for driving system shutdown, LED indicators, or MCU interrupts
