# program solve a puzzle of murder mystery
# clue game

import termcolor

from logic import *

mustard = Symbol("Col.Mustard")
plum = Symbol("Prof.Plum")
scarlet = Symbol("Ms.Scarlet")
characters = [mustard, plum, scarlet]

ballroom = Symbol("ballroom")
kitchen = Symbol("kitchen")
library = Symbol("library")
rooms = [ballroom, kitchen, library]

knife = Symbol("knife")
revolver = Symbol("revolver")
wrench = Symbol("wrench")
weapons = [knife, revolver, wrench]

symbols = characters + rooms + weapons


def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: YES", "green")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")

knowledge = And(
    Or(mustard, plum, scarlet),
    Or(ballroom, kitchen, library),
    Or(knife, revolver, wrench)
)

knowledge.add(Implication(
    And(mustard, ballroom),
    And(Not(knife), kitchen)
))

knowledge.add(And(
    And(plum, wrench),
    library
))

knowledge.add(Biconditional(
    scarlet, 
    And(Not(kitchen), Implication(revolver, ballroom))
))

knowledge.add(And(
    And(wrench, Not(library)),
    Implication(And(plum, mustard), ballroom)
))

check_knowledge(knowledge)