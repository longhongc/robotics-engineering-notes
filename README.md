# Robotics Engineering Notes

Personal notes for learning the mathematical foundations and engineering practice of robotics. The collection currently starts with linear algebra and will grow to cover optimization, control, planning, probability, and modeling.

## Repo structure
- `raws/`: source notes, organized by subject.
- `raws/linear-algebra/`: linear algebra foundations.
- `raws/optimization/`: numerical and mathematical optimization.
- `raws/control/`: dynamical systems and control foundations.
- `raws/planning/`: graph theory, game theory, and reinforcement learning.
- `raws/probability/`: probability, statistics, and estimation.
- `raws/modeling/`: robot modeling, including dynamics and system identification.
- `docs/`: MkDocs site root (`index.md` lives here).
- `docs/notes/`: generated MkDocs-compatible notes (mainly for LaTeX syntax).
- `format_raw_to_docs.py`: script that converts `raws/` into `docs/notes/`.
- `mkdocs.yml`: MkDocs configuration.

## Current resources
### Books
- Sheldon Axler, *Linear Algebra Done Right*.
- Gilbert Strang, *Linear Algebra and Its Applications*.

### Video series
- 3Blue1Brown, [*Essence of Linear Algebra* (YouTube)](https://youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&si=ULx7NuL18mrh5fla).
- Visual Kernel, [*Matrix* series (YouTube)](https://youtube.com/playlist?list=PLWhu9osGd2dB9uMG5gKBARmk73oHUUQZS&si=9g14KcG363GJ7BHS).

## Notes

The project is organized around robotics subjects rather than a fixed course sequence. Add new source material under the most specific matching folder; create a subfolder when a subject grows large enough to need one.

To rebuild the rendered notes, update content in `raws/` and run:

```bash
python format_raw_to_docs.py --clean
```
