| Net Name         | Connected To             | Description                          |
|------------------|--------------------------|--------------------------------------|
| RF_OUT           | Output Transformer       | Amplifier output to LPF or load      |
| TP1              | BiasControl_IRF640       | Bias voltage monitor (0.9V ±0.3V)    |
| +12Vcc           | Power Supply             | Main supply rail for output stage    |
| GND              | System Ground            | Common reference                     |
| Parameter         | Value                                |
|-------------------|--------------------------------------|
| Core              | Fair-Rite #5961003801-102            |
| Primary Winding   | AWG#18, 8 turns, center-tapped       |
| Secondary Winding | RF_OUT → LPF or dummy load           |
| Winding Type      | Bifilar or Trifilar                  |
| Turns Ratio       | 3:2 or 1:1 (based on impedance/power)|

Integration Notes
Bias Monitoring: TP1 feeds into BiasFaultBlock

Output Routing: RF_OUT connects to LPF_BandSelect block

Transformer Guidance: Embedded notes make replication easy for collaborators
