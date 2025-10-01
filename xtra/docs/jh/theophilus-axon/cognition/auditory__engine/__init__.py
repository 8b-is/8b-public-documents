"""
auditory_engine/__init__.py

Initializes the auditory engine module for symbolic auditory perception.
This includes:
- FFT-based interpretation (waveform → symbols)
- Breath rhythm processing
- Auditory to SPC mapping
- Spatial anchoring of sound events

All auditory streams are routed through UDC-compliant modules.
"""

from .fft_wave_interpreter import *
from .auditory_integration import *
from .auditory_symbol_mapper import *
from .breath_cycle_simulator import *
from .spatial_memory_anchor import *
from .real_time_stub import *
