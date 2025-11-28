#!/usr/bin/zsh
alias python='python3'

python color_scheme_driver.py                                 \
--scheme_type gnome                                           \
--file        sample-themes/flux-bunny-dark-bright/flux-bunny-dark-bright-input.json    \
--out_dir     sample-themes/flux-bunny-dark-bright                         \
--name        bar
