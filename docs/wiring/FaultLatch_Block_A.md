
| Net Name           | Connected To             | Description                          |
|--------------------|--------------------------|--------------------------------------|
| QUI_FaultDetected  | FaultAggregation_Block   | Triggers latch when HIGH             |
| QUI_LatchReset     | Manual or MCU input      | Resets latch when HIGH               |
| QUI_FaultLatched   | RelayControl_Block, LED  | Held HIGH until reset                |
Integration Notes
Input Source: Aggregated fault signal from OR gate

Output Destination: Relay mute logic, LED indicator, fault monitor

Logic Summary: Cross-coupled gates form a feedback loop that holds the fault state
