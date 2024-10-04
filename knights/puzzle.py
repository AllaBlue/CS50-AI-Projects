from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    
    # Character cannot be a knave and a knight at the same time
    Or(And(AKnight, Not(AKnave)), And(AKnave, Not(AKnight))),

    # Knave always lies
    Implication(AKnave, Not(And(AKnave, AKnight))),

    # Knight always says true
    Implication(AKnight, And(AKnave, AKnight))

)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(

    # Character cannot be a knave and a knight at the same time
    Or(And(AKnight, Not(AKnave)), And(AKnave, Not(AKnight))),
    Or(And(BKnight, Not(BKnave)), And(BKnave, Not(BKnight))),

    # Knave always lies
    Implication(AKnave, Not(And(AKnave, BKnave))),
    
    # Knight always says true
    Implication(AKnight, And(AKnave, BKnave))
    
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(

    # Character cannot be a knave and a knight at the same time
    Or(And(AKnight, Not(AKnave)), And(AKnave, Not(AKnight))),
    Or(And(BKnight, Not(BKnave)), And(BKnave, Not(BKnight))),

    # Knight always tells the truth
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(BKnight, Or(And(AKnight, BKnave), And(BKnight, AKnave))),

    # Knave always lies
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(BKnight, AKnave))))

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    
    # Character cannot be a knave and a knight at the same time
    Or(And(AKnight, Not(AKnave)), And(AKnave, Not(AKnight))),
    Or(And(BKnight, Not(BKnave)), And(BKnave, Not(BKnight))),
    Or(And(CKnight, Not(CKnave)), And(CKnave, Not(CKnight))),

    # Knight always tells the truth
    Implication(AKnight, Or(AKnight, AKnave)),
    Implication(BKnight, And(Or(Implication(AKnight, AKnave), 
                                Implication(AKnave, Not(AKnave))), CKnave)),
    Implication(CKnight, AKnight),

    # Knave always lies
    Implication(AKnave, Not(Or(AKnight, AKnave))),
    Implication(BKnave, Not(
        And(Or(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave))), CKnave))),
    Implication(CKnave, Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()