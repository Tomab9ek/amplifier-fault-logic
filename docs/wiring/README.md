
🎯

🧠 Amplifier Fault Logic System — Wiring Overview
Welcome to the modular fault logic documentation for your amplifier system. This repo contains a set of fault detection blocks — each independently documented and wired — that work together to monitor bias, thermal, and overcurrent conditions. Faults are latched and relayed for diagnostics and protection.

📦 Block-Level Wiring Tables
Block Name	Description	Link
BiasFaultBlock	Monitors bias voltage and flags out-of-range	BiasFaultBlock.md
ThermalFaultBlock	Detects overheating via thermistor comparator	ThermalFaultBlock.md
OvercurrentFaultBlock	Flags excessive current draw using shunt sensing	OvercurrentFaultBlock.md
FaultLatch_Block_A	Holds fault state until reset	FaultLatch_Block_A.md
FinalStage_IRF640	Amplifier output stage and bias monitoring	FinalStage_IRF640.md
🔗 Signal Flow Summary
Analog Inputs: Bias, current, and temperature are monitored via comparators

Fault Outputs: Active HIGH signals feed into FaultAggregation_Block

Latch Logic: Faults are held until reset via FaultLatch_Block_A

Relay Control: Latched faults mute output and trigger LED indicators

Test Points: Embedded across blocks for diagnostics and calibration
