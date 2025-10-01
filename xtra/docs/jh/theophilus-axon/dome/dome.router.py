# dome.route.py

"""
Routes spatial and temporal memory blocks through the Dynamic Object Memory Environment (DOME).
Simulates biological routing pathways used in cortical and subcortical regions to form context-rich,
location-aware, and temporally coherent memory frames.

SCIENTIFIC BASIS:
- Routing across space and time is analogous to hippocampal-cortical memory pathways (Buzsáki, 2005).
- Spatial tagging builds contextual awareness through distributed neuron-like memory anchoring (Eichenbaum, 2004).
- Temporal anchors align memory formation to internal circadian and event-based clocks (McClelland et al., 1995).

UDC COMPLIANCE:
✔ Links memory blocks via recursive spatial and temporal anchors.
✔ Complies with the symbolic layering requirement of memory trace recursion.
✔ Provides spatial identity and continuity — a critical element for time-delay consciousness loops.

REFERENCES:
- Buzsáki, G. (2005). Theta rhythm of navigation: link between path integration and landmark navigation. *Hippocampus*, 15(7), 827–840.
- Eichenbaum, H. (2004). Hippocampus: Cognitive processes and neural representations that underlie declarative memory. *Neuron*, 44(1), 109–120.
- McClelland, J. L., McNaughton, B. L., & O’Reilly, R. C. (1995). Why there are complementary learning systems in the hippocampus and neocortex. *Psychological Review*, 102(3), 419–457.
"""

from DOME.temporal_anchor import add_temporal_anchor
from DOME.spatial_context import add_spatial_context
from DOME.grid_mapper import map_to_3d_grid

def process_memory_block(memory_block, location="sensor-A"):
    """
    Augments a memory block with temporal, spatial, and grid-mapped coordinates for contextual anchoring.

    Args:
        memory_block (dict): The raw memory block being processed.
        location (str): Sensor origin, spatial tag, or semantic label of memory origin.

    Returns:
        dict: Fully processed memory block with temporal, spatial, and grid routing.
    """
    memory_block = add_temporal_anchor(memory_block)
    memory_block = add_spatial_context(memory_block, location)
    memory_block = map_to_3d_grid(memory_block)
    return memory_block
