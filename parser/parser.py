import nltk
import sys
nltk.download('punkt')
nltk.download('punkt_tab')

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP | NP VP Conj VP | S Conj S 
NP -> N | Adj NP | P NP | Det NP | Adv NP | NP P | N NP
VP -> V | V NP | VP NP | Adv VP | V Adv 
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    tokens = nltk.tokenize.word_tokenize(sentence)

    for i, token in enumerate(tokens):
        tokens[i] = tokens[i].lower()
        if not token.isalpha():
            tokens.remove(token)
    
    return tokens


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    np_chunks = []

    # For every subtree in a tree check if it is a Noun Phrase (NP)
    for subtree in tree.subtrees():
        if subtree.label() == "NP":
            flag = True
            # For every subtree in this subtree check if at least one of this subtrees is a Noun Phrase (NP)
            # If yes, then we do not add the parent subtree to the np_chunks
            for i, subsub in enumerate(subtree.subtrees()):
                if i == 0:
                    continue
                if subsub.label() == "NP":
                    flag = False
            # If there is no Noun Phrase in the subtree then add this subtree to the np_chunks
            if flag:
                np_chunks.append(subtree)
    return np_chunks


if __name__ == "__main__":
    main()