# Relay Feedback Block

## Overview
This block monitors the physical state of the relay output and compares it to the control signal. It flags a fault if the relay fails to respond correctly to control commands.

## Inputs
| Signal Name     | Description                          | Type    |
|----------------|--------------------------------------|---------|
| RELAY_CTRL      | Command signal to activate relay     | Digital |
| RELAY_SENSE     | Voltage sensed at relay contact      | Digital |

## Outputs
| Signal Name     | Description                          | Type    |
|----------------|--------------------------------------|---------|
| RELAY_FAULT     | Fault output signal (active-high)     | Digital |

## Logic Description
- Compares `RELAY_CTRL` vs `RELAY_SENSE`
- If mismatch persists for defined debounce period, `RELAY_FAULT` goes high
- Can be latched externally or passed to fault aggregator

## Notes
- Use XOR gate or comparator logic
- Add debounce or delay to avoid false positives during switching
- Useful for detecting stuck contacts, wiring faults, or control mismatches
