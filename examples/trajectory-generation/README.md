# Trajectory-generation example

`generate_path_timing_figure.py` simulates a path with a constant nominal
path-coordinate velocity. A multiplier slows the path to a stop while the
script chooses a conservative path acceleration that keeps the scalar output
acceleration below the configured limit.

The straight-line path is the primary teaching example. The sine path is an
extension that shows the additional path-curvature acceleration term.

Install the example-only dependencies into the repository virtual environment:

```bash
uv pip install --python .venv/bin/python \
  -r examples/trajectory-generation/requirements.txt
```

Generate the repository SVG asset:

```bash
MPLCONFIGDIR=/tmp/robotics-engineering-notes-mpl \
  ./.venv/bin/python \
  examples/trajectory-generation/generate_path_timing_figure.py
```

Generate the curved-path extension:

```bash
MPLCONFIGDIR=/tmp/robotics-engineering-notes-mpl \
  ./.venv/bin/python \
  examples/trajectory-generation/generate_path_timing_figure.py \
  --path sine
```

The script also accepts `--output` for local PNG inspection. The example is
educational and does not model jerk, torque, actuator, or multi-joint limits.
The multiplier and path-progress panels use dots to mark every tenth discrete
controller sample; the connecting lines are only visual guides.
