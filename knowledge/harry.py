from logic import *

rain = Symbol("rain") # it is raining
hagrid = Symbol("hagrid") # harray visited hagrid
dumbledore = Symbol("dumbledore") # harry visited dumbledore

knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)

print(model_check(knowledge, rain))
# print(sentance.validate(sentance))