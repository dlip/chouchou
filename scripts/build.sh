#!/usr/bin/env bash
set -euo pipefail

npm exec ergogen -- .
cp output/pcbs/chouchou.kicad_pcb kicad/
npm exec openjscad -- output/cases/bottom.jscad -of stla -o output/cases/bottom.stl
# fstl output/cases/bottom.stl