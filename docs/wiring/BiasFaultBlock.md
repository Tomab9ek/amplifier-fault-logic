| Net Name         | Connected To             | Description                          |
|------------------|--------------------------|--------------------------------------|
| Bias_Sense_X     | TP1, TP2, ...            | Bias voltage inputs from power stage |
| Comparator_Out   | LM393 open-drain output  | Fault signal to aggregation block    |
| QVL_BiasFault    | FaultAggregation_Block   | Active HIGH fault output             |
Integration Notes
Input Source: Bias voltages from BiasControl_IRF640

Output Destination: OR gate input on FaultAggregation_Block

Threshold Logic: Comparator trips when bias voltage is outside 0.6V–1.2V range
