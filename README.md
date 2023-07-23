# Chouchou keyboard

This is WIP (Please don't use until I can test everything)

Chouchou (Japanese for butterfly) is a minimalist unibody keyboard designed to be used with the [Taipo](https://inkeys.wiki/en/keymaps/taipo) layout.
It uses a cheap RP2040-Zero MCU and requires no diodes since the 20 edge pinouts it provides is the exact number of keys Taipo requires.

## Build Your Own

### Board

#### Parts

- Send the [Gerber](kicad/gerber_to_order) file to the PCB manufacturer of your choice
- 1 x RP2040-Zero
- 20 x low profile choc switches and keycaps
- (optional) 20 x kailh hotswap sockets
- (optional) RP2040-Zero headers

#### Instructions

- Solder the RP2040-Zero to the board either directly or using the headers you purchased
- Build and flash the [QMK firmware](https://github.com/dlip/qmk_firmware/tree/chouchou/keyboards/chouchou)
- You can test the keyboard at this point by connecting the hotswap pads with some metal tweezers before continuing
- Solder the kalih hotswap sockets if purchased or solder the switches directly the board otherwise
- Insert the switches into the hotswap sockets if necessary
- Add your keycaps 

### Case

#### Parts

- 3D print the [case.stl](case/case.stl) file
- 8 x Knurled Insert Nuts (M2 x 3mm Length x 3.2mm OD) [example](https://www.amazon.com/dp/B07LBQFNQD)
- 8 x M2 3mm flat screws [example](https://www.amazon.com/gp/product/B01FTI8TM8/) 

#### Instructions

- Use a soldering iron to melt the insert nuts into the holes in the case
- Screw the board to the case