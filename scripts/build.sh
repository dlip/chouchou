#!/usr/bin/env bash
set -euo pipefail

npm exec ergogen -- .
cp output/pcbs/chouchou.kicad_pcb kicad/
for i in output/cases/*.jscad; do npm exec openjscad -- "$i" -of stla; done
# fstl output/cases/bottom.stl