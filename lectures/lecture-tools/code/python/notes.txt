diff

diff -u iteration1.py iteration2.py > iteration.patch

patch iteration1.py iteration.patch

version control

generation of version control

static checking

runtime

profiling

debugging

IDEs


debug

import pdb; pdb.set_trace()

3.7: breakpoint()

commandline: python -m pdb script.py





ORDER OF OPERATIONS:
PROFILE
python -m cProfile -s time 1_particles.py

DEBUG
Add to event handling:
  elif event.type == pygame.KEYDOWN:
    import pdb; pdb.set_trace()

- print(particles)
- print(particles[0])
- print(particles[0].direction)
- print(particles[0].speed)

PEP8:
pycodestyle 4_particles_nonbuggy.py
 show with --show_pep8


pympler

import pympler.tracker

#before main loop
mem = pympler.tracker.SummaryTracker()


# on quit
mem.print_diff()
