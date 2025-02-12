#!/usr/bin/env python3

"""
rlwrap filter for llm-chat that automatically wraps multi-line input
in !multi markers
"""

import sys
import os

if 'RLWRAP_FILTERDIR' in os.environ:
    sys.path.append(os.environ['RLWRAP_FILTERDIR'])
else:
    sys.path.append('.')

import rlwrapfilter

filter = rlwrapfilter.RlwrapFilter()

def handle_input(input_text):
    """Wrap multi-line input in !multi markers"""
    input_text = input_text.strip()
    if "\n" in input_text and not input_text.startswith("!multi"):
        return f"!multi\n{input_text}\n!end"
    return input_text

filter.help_text = '\n'.join([
    "Usage: rlwrap -z {0} llm chat".format(__file__),
    "Automatically wraps multi-line input in !multi markers for llm chat"
])

filter.input_handler = handle_input

# Pass through output unchanged but track it for prompt handling
filter.output_handler = lambda output: output

filter.run()
