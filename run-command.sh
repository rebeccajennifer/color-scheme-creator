#!/usr/bin/zsh
alias python='python3'
python color_scheme_driver.py                                 \
--scheme_type gnome                                           \
--file        sample-themes/flux-dark/flux-dark-input.json    \
--out_dir     sample-themes/flux-dark                         \
--name        bar
