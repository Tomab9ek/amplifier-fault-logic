# Relay Fault Block

## Overview
This block monitors the state of a relay and triggers a fault signal if the relay fails to switch as expected. It compares control logic with sensed output to detect discrepancies.

## Inputs
| Signal Name     | Description                          | Voltage Level |
|----------------|--------------------------------------|---------------|
| RELAY_CTRL      | Logic signal commanding relay state   | Digital       |
| RELAY_SENSE     | Voltage sensed at relay output        | Analog/Digital|

## Outputs
| Signal Name     | Description                          | Type          |
|----------------|--------------------------------------|---------------|
| RELAY_FAULT     | Fault output signal (active-high)     | Digital       |

## Logic Description
- Compares `RELAY_CTRL` vs `RELAY_SENSE`
- If mismatch persists beyond debounce window, `RELAY_FAULT` goes high
- Fault signal can be latched or passed to aggregator

## Notes
- Add debounce or delay to avoid false positives during switching
- Useful for detecting stuck contacts, wiring faults, or control mismatches
