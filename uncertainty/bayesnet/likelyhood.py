from model import model

# create probability where respective events will be
probability = model.probability([["none", "no", "on time", "attend"]])

print(probability)
