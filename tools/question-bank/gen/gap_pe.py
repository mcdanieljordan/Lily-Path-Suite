#!/usr/bin/env python3
"""Physical Education K-5 gap fill: outdoor pursuits (K, G1) and rhythmic activities (G4, G5)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('116.', 926, own='gap_pe.jsonl')

load(B, """
12.b.7|2|Which is a fun outdoor activity a kindergartner can do at a park?|playing on a playground|doing homework in bed|watching TV|sleeping in a closet|Parks offer outdoor play.
12.b.7|2|When you play outside on a hot day, it is smart to take breaks in the...|shade|hot sun|car|oven|Shade helps you cool down.
13.b.7|2|Which outdoor activity is a good way to explore nature with a grown-up?|walking on a trail|staying in a dark room|playing video games|sleeping|Trails show you nature.
13.b.7|2|On a nature walk, you should stay on the trail so you...|do not get lost|hide|run into traffic|pick every flower|Trails keep you safe.
16.b.5|3|Which dance style uses a group pattern like a line or a square set to music?|a folk dance|a nap|a race|a quiz|Folk dances use set patterns.
16.b.5|3|When you keep your movements in time with music, you are showing...|rhythm|stillness|silence|sleep|Rhythm matches the beat.
16.b.5|3|A jump rope routine done to music uses...|a rhythm pattern|no beat|a race|random jumping|Routines follow a rhythm.
17.b.5|4|A dance routine that repeats steps in a set pattern to music is a...|choreographed sequence|random shuffle|nap|rest|Choreography organizes movement.
17.b.5|4|Keeping the tempo of a dance means you...|move at the speed of the music|stop|move randomly|run away|Tempo is the speed of the beat.
17.b.5|4|Working with a group to create a rhythmic routine requires...|cooperating and counting beats together|working alone|ignoring the music|arguing|Groups count the beat.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'gap_pe.jsonl'))
print("saved", len(B.out), "questions")
