# Robotics Engineering Notes

Personal notes for learning the mathematical foundations and engineering practice of robotics. The collection currently starts with linear algebra and will grow to cover optimization, control, planning, probability, and modeling.

The notes are organized by subject so that mathematical foundations and robotics applications can grow together.

## Repo structure
- `raws/`: source notes, organized by subject.
- `raws/linear-algebra/`: linear algebra foundations.
- `raws/optimization/`: numerical and mathematical optimization.
- `raws/control/`: dynamical systems and control foundations.
- `raws/planning/`: graph theory, game theory, and reinforcement learning.
- `raws/probability/`: probability, statistics, and estimation.
- `raws/modeling/`: robot modeling, including dynamics and system identification.
- `docs/`: MkDocs site root (`index.md` lives here).
- `docs/notes/`: generated MkDocs-compatible notes.
- `format_raw_to_docs.py`: script that converts `raws/` into `docs/notes/`.
- `mkdocs.yml`: MkDocs configuration.

## Notes

- [Linear algebra](notes/linear-algebra/index.md)
- [Optimization](notes/optimization/index.md)
- [Control](notes/control/index.md)
- [Planning](notes/planning/index.md)
- [Probability](notes/probability/index.md)
- [Modeling](notes/modeling/index.md)

## Current resources
### Books
- Sheldon Axler, *Linear Algebra Done Right*.
- Gilbert Strang, *Linear Algebra and Its Applications*.

### Linear algebra

- 3Blue1Brown, [*Essence of Linear Algebra* (YouTube)](https://youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&si=ULx7NuL18mrh5fla).
- Visual Kernel, [*Matrix* series (YouTube)](https://youtube.com/playlist?list=PLWhu9osGd2dB9uMG5gKBARmk73oHUUQZS&si=9g14KcG363GJ7BHS).

### Control

- Brian Douglas, [*Classical Control Theory* (YouTube)](https://www.youtube.com/watch?v=oBc_BHxw78s&list=PLUMWjy5jgHK1NC52DXXrriwihVrYZKqjk&pp=iAQB).
- Steve Brunton, [*Control Bootcamp* (YouTube)](https://www.youtube.com/watch?v=Pi7l8mMjYVE&list=PLMrJAkhIeNNR20Mz-VpzgfQs5zrYi085m).

### Optimization

- Steve Brunton, [*Optimization Bootcamp* (YouTube)](https://www.youtube.com/watch?v=lPBPbGmw1_4&list=PLMrJAkhIeNNS3UT10txhV70ZwIeIjkMQp).

## Planned resources

### Control

- Karl Johan Åström and Richard M. Murray, [*Feedback Systems: An Introduction for Scientists and Engineers*](https://www.cds.caltech.edu/~murray/FBS/Second_Edition.html) (2nd Edition).

### Optimization

- Jorge Nocedal and Stephen J. Wright, [*Numerical Optimization*](https://link.springer.com/book/10.1007/978-0-387-40065-5) (2nd Edition).
- Stephen Boyd and Lieven Vandenberghe, [*Convex Optimization*](https://web.stanford.edu/~boyd/cvxbook/).

### Modeling

- Mark W. Spong, Seth Hutchinson, and M. Vidyasagar, [*Robot Modeling and Control, 2nd Edition*](https://www.wiley-vch.de/en/?isbn=978-1-119-52399-4&option=com_eshop&view=product).
- Kevin M. Lynch and Frank C. Park, [*Modern Robotics: Mechanics, Planning, and Control*](https://www.cambridge.org/core/books/modern-robotics/57C3BB1C6D5CB40320FA96E5FA3BCEC6).

Update content in `raws/` and run `python format_raw_to_docs.py --clean` to regenerate `docs/notes/`.
