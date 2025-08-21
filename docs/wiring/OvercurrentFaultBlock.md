| Net Name             | Connected To             | Description                          |
|----------------------|--------------------------|--------------------------------------|
| Overcurrent_Sense    | Across R_Shunt           | Voltage drop for fault detection     |
| Comparator_Output    | LM393 open-drain output  | Fault signal to aggregation block    |
| QUI_OvercurrentFault | FaultAggregation_Block   | Active HIGH fault output             |
Integration Notes
Input Source: Shunt resistor voltage drop

Output Destination: OR gate input on FaultAggregation_Block

Trip Logic: Fault triggers when 
𝑉
shunt
>
𝑉
threshold
, e.g. 100mV across 0.1Ω = 1A
