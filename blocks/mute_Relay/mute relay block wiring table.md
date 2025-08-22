## Mute Relay Block Wiring Table

| Signal Name         | Source                  | Destination           | Notes                                  |
|---------------------|-------------------------|------------------------|----------------------------------------|
| `MUTE_CTRL`         | MCU.PIN_A3              | OR3.IN1                | Manual mute control                    |
| `FAULT_AGG`         | fault_aggregator.OUT    | OR3.IN2                | Aggregated fault signal                |
| `POWER_ON_RESET`    | startup_delay.OUT       | OR3.IN3                | Startup mute delay                     |
| `ENABLE`            | system_enable.OUT       | AND1.IN1               | System enable gate                     |
| `OR3_OUT`           | OR3.OUT                 | AND1.IN2               | Combined mute condition                |
| `RELAY_MUTE_DRV`    | AND1.OUT                | relay_driver.IN        | Drives mute relay                      |
| `STATUS_MUTE_ACTIVE`| relay_driver.OUT        | MCU.PIN_B1             | Indicates mute is active               |


🧠 Schematic Notes
Use a 3-input OR gate (e.g., 74HC4075) for combining mute triggers.

AND gate ensures mute only activates when system is enabled.

Relay driver can be a NPN transistor or comparator with hysteresis.

Add a flyback diode across the relay coil.

Optional: LED indicator tied to STATUS_MUTE_ACTIVE.