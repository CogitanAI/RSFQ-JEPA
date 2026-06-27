# Cell JSON Schema

This document describes the JSON schema for an RSFQ logic cell submitted to RSFQ-JEPA. Each cell is a single JSON object with the top-level fields below.

## Top-level fields

| Field | Type | Description |
| --- | --- | --- |
| `cell_id` | string | Unique identifier for the cell, e.g. `"RSFF_DEMO_001"`. |
| `cell_type` | string | Logic cell type, e.g. `"JTL"`, `"DFF"`, `"AND2"`. |
| `source_pdk` | string | Process design kit the cell targets, e.g. `"MIT-LL SFQ5ee+"`. |
| `physical_stack` | object | Physical layout and process description. See below. |
| `josephson_junctions` | array | List of Josephson junction (JJ) objects. See below. |
| `superconducting_loops` | array | List of superconducting loop objects. See below. |
| `electrical_parameters` | object | Cell-level electrical parameters. |

## `physical_stack` (object)

| Field | Type | Description |
| --- | --- | --- |
| `process_node` | string | Process node identifier. |
| `bounding_box_um` | object or array | Cell bounding box dimensions in micrometers. |
| `layers` | array | Layer entries describing the physical stack. |

## `josephson_junctions` (array)

An array of JJ objects. Each JJ object includes:

| Field | Type | Description |
| --- | --- | --- |
| `position` | object or array | JJ position within the cell. |
| `critical_current` | number | Critical current (Ic) of the junction. |

## `superconducting_loops` (array)

An array of loop objects. Each loop object includes:

| Field | Type | Description |
| --- | --- | --- |
| `loop_inductance` | number | Inductance of the superconducting loop. |

## `electrical_parameters` (object)

Cell-level electrical parameters used as inputs to the surrogate.

## Worked examples

Complete worked examples are provided in:

- `examples/RSFF_DEMO_001.json`
- `examples/PA_DEMO_001.json`
