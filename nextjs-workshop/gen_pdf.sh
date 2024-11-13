#!/usr/bin/env sh

# This, or simply use Chrome Print and get better results lol

output=${1:-"pdf/Presentation.pdf"}
url="http://localhost:9911"

decktape -s 1280x720 remark $url $output