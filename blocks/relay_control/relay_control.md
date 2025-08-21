# Relay Control Block

## Overview
This block provides control logic for activating a relay based on system conditions or MCU commands. It interfaces with the relay driver and monitors feedback for fault detection.

## Inputs
| Signal Name     | Description                          | Type    |
|----------------|--------------------------------------|---------|
| RELAY_ENABLE    | Command signal to activate relay     | Digital |
| FAULT_LATCHED   | Global fault signal (inhibit relay)  | Digital |

## Outputs
| Signal Name     | Description                          | Type    |
|----------------|--------------------------------------|---------|
| RELAY_CTRL      | Output to relay driver               | Digital |
| RELAY_STATUS    | Optional feedback from relay contact | Digital |

## Logic Description
- `RELAY_CTRL = RELAY_ENABLE AND NOT FAULT_LATCHED`
- Relay is only activated if no latched fault is present
- `RELAY_STATUS` can be used for fault comparison (see `relay_fault` block)

## Notes
- Use open-drain or push-pull driver depending on relay specs
- Add snubber or flyback diode if mechanical relay is used
