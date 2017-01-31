# dxlctl - Dynamixel control.

See the python library or the Dynamixel documentation for more info.

Documentation links:  [AX-12A](http://support.robotis.com/en/product/actuator/dynamixel/ax_series/dxl_ax_actuator.htm), [MX-28](http://support.robotis.com/en/product/actuator/dynamixel/mx_series/mx-28.htm), [MX-64](http://support.robotis.com/en/product/actuator/dynamixel/mx_series/mx-64.htm).

[FTDI drivers](http://www.ftdichip.com/Drivers/VCP.htm)

## Serial Protocol

The protocol is very thin, and only exposes register reads and writes.

Commands are single lines which start with a character `'C'`.

Responses are single lines which start with a character `'R'`.

Lines contain comma-separated integers and end with newlines `'\n'`.

### Get Register `'Cg'`, `'CG'`

*Get Register* reads a register value from Dynamixel ID `<id>` at address `<reg>`.
Lower-case `'g'` indicates a single-byte register, capital `'G'` indicates two bytes.

    Cg<id>,<reg>
    CG<id>,<reg>

See the Dynamixel documentation for register tables and addresses.

### Set Register `'Cs'`, `'CS'`

*Set Register* sets a register on Dynamixel ID `<id>` at address `<reg>` to value `<val>`.
Lower-case `'s'` indicates a single-byte register, capital `'S'` indicates two bytes.

    Cs<id>,<reg>,<val>
    CS<id>,<reg>,<val>

The response to the set register command is the same as if it were called with get.

### Response `'R'`

The response to any command is to read back the register value.

*Response* returns the Dynamixel ID `<id>` at address `<reg>` value `<val>`.

    R<id>,<reg>,<val>

For now it actually reads the value, so writes can be observed.
