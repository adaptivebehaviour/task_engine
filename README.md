# Task Engine

A Streamlit-based workbench for designing and prototyping the underlying mechanics of behavioural tasks.

## What it is

A behavioural task is a structured activity used to measure a psychological or behavioural construct — for example, risk tolerance, cognitive flexibility, or delay discounting. Getting the mechanics right (scoring rules, trial sequencing, adaptive logic, boundary conditions) before building a polished interface saves significant time.

The task engine provides a live, interactive environment for iterating on that logic. You build and test the core mechanics here; the resulting design becomes the specification for whatever final product (serious game, lab task, app) you are building.

## Workflow

1. **Fork or copy this repository** to create a clean workspace for your task.
2. **Open `app.py`** and implement your task mechanics inside the Streamlit app.
3. **Run the app** and interact with your task to verify behaviour.
4. Iterate until the mechanics are correct, then use the validated logic as the basis for your production implementation.

Do not develop tasks directly in this repository. Always work in a copy so the template stays clean for future projects.

## Running the app

```bash
pip install streamlit
streamlit run app.py
```

Or use the VS Code launch configuration (F5 → Launch).

## Project structure

```
task_engine/
├── app.py          # Main Streamlit app — implement your task here
├── .vscode/
│   ├── launch.json # VS Code debug/run configuration
│   └── app.bat     # Launch script
└── README.md
```

## Example use cases

- Risk tolerance task: present a series of gambles; record choices; fit a utility model.
- Go/No-Go task: trial sequencing, response window timing, miss/false-alarm scoring.
- Balloon Analogue Risk Task (BART): pump logic, explosion probability, bank mechanics.
- Delay discounting: indifference-point elicitation, adaptive staircase.
