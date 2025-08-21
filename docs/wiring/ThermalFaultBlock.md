| Net Name         | Connected To             | Description                          |
|------------------|--------------------------|--------------------------------------|
| IN_Thermistor    | TH1L10L, R1              | Temperature sensing input            |
| IN_Threshold     | R2, R4                   | Reference voltage for comparator     |
| Comparator_Out   | LM393 open-drain output  | Fault signal to aggregation block    |
| OUT_ThermalFault | FaultAggregation_Block   | Active HIGH fault output             |

Integration Notes
Input Source: Thermistor voltage divider

Output Destination: OR gate input on FaultAggregation_Block

Trip Logic: Comparator triggers when thermistor voltage drops below threshold (indicating high temperature)
