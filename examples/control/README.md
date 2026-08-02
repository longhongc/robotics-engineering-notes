# Frequency-response example

\`generate_resonance_frequency_figure.py\` generates the three-panel SVG used in
the second-order frequency note. It compares the normalized displacement gain
for an undamped oscillator, a lightly damped oscillator, and a strongly damped
oscillator whose displacement response has no nonzero resonance peak.

Install the example-only dependencies into the repository virtual environment:

\`\`\`bash
uv pip install --python .venv/bin/python \
  -r examples/control/requirements.txt
\`\`\`

Generate the source asset from the repository root:

\`\`\`bash
MPLCONFIGDIR=/tmp/robotics-engineering-notes-mpl \
  ./.venv/bin/python examples/control/generate_resonance_frequency_figure.py
\`\`\`

The default output is
\`raws/control/assets/resonance-frequency-response.svg\`. Pass \`--output\` to
write an alternate SVG or PNG for local inspection.
