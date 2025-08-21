# Bias Control Block

## Overview
This block controls the activation of the amplifier bias rail. It enables bias voltage only when system conditions are safe (no latched faults) and optionally after a startup delay.

## Inputs
| Signal Name       | Description                          | Type    |
|-------------------|--------------------------------------|---------|
| ENABLE_BIAS       | Command signal from MCU              | Digital |
| FAULT_LATCHED     | Global fault signal (inhibit bias)   | Digital |
| POWER_GOOD        | Optional system power OK signal      | Digital |

## Outputs
| Signal Name       | Description                          | Type    |
|-------------------|--------------------------------------|---------|
| BIAS_CTRL         | Output to bias regulator or switch   | Digital |

## Logic Description
- `BIAS_CTRL = ENABLE_BIAS AND POWER_GOOD AND NOT FAULT_LATCHED`
- Bias rail is only enabled when system is ready and fault-free
- Optional: Add delay or sequencing logic for soft-start

## Notes
- Use open-drain or push-pull driver depending on regulator
- Consider adding fault override or manual disable input
