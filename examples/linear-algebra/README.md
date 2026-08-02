# Jordan-chain diagram example

\`generate_jordan_chain_diagram.py\` generates the state-space block diagram
used in the Jordan-form note. It shows the two-state system

\[
\dot{x}_1=\lambda x_1+x_2,\qquad
\dot{x}_2=\lambda x_2
\]

as two feedback-integrator stages with one-way coupling from \(x_2\) to
\(x_1\).

Install the example-only dependency into the repository virtual environment:

\`\`\`bash
uv pip install --python .venv/bin/python matplotlib
\`\`\`

Generate the source asset from the repository root:

\`\`\`bash
MPLCONFIGDIR=/tmp/robotics-engineering-notes-mpl \
  ./.venv/bin/python examples/linear-algebra/generate_jordan_chain_diagram.py
\`\`\`

The default output is
\`raws/linear-algebra/assets/jordan-block-integrator-chain.svg\`. Pass
\`--output\` to write an alternate SVG for local inspection.
