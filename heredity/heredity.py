import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity/heredity.py heredity/data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """

    # P(zero_genes, one_gene, two_genes, no_traits, have_traits)

    zero_genes = set(
        [person for person in people if person not in one_gene and person not in two_genes])
    no_traits = set([person for person in people if person not in have_trait])
    
    probability = 1
    for person in zero_genes:
        probability = probability * get_probability_of_person_has_gene(
            people=people, person=person, gene=0, one_gene=one_gene, two_genes=two_genes, zero_genes=zero_genes)
    
    for person in one_gene:
        probability = probability * get_probability_of_person_has_gene(
            people=people, person=person, gene=1, one_gene=one_gene, two_genes=two_genes, zero_genes=zero_genes)
        
    for person in two_genes:
        probability = probability * get_probability_of_person_has_gene(
            people=people, person=person, gene=2, one_gene=one_gene, two_genes=two_genes, zero_genes=zero_genes)
        
    for person in no_traits:
        probability = probability * get_probability_of_person_has_trait(
            people=people, person=person, trait=False, zero_genes=zero_genes, one_gene=one_gene, two_genes=two_genes)
    
    for person in have_trait:
        probability = probability * get_probability_of_person_has_trait(
            people=people, person=person, trait=True, zero_genes=zero_genes, one_gene=one_gene, two_genes=two_genes)
    
    return probability


def get_joint_child_gene_probability_by_mother_father(mother_gene, father_gene, child_gene, mutation):
    # CG means child_gene
    # MG means mother_gene
    # FG means father_gene
    # probability = P(CG = child_gene | MG = mother_gene, FG = father_gene) with mutation probability
    probability = 0

    # calculate the probability that child has 0 genes:
    if child_gene == 0:
        # If child_gene = 0, then both genes of parents did not pass

        # If gene = 2, then it did not pass and mutated
        # If gene = 1, then it did not pass with 50% probability
        # If gene = 0, then it did not pass and did not mutate

        if mother_gene == 2 and father_gene == 2:
            probability = mutation * mutation

        elif (mother_gene == 2 and father_gene == 1) or (father_gene == 2 and mother_gene == 1):
            probability = mutation * 0.5
            
        elif mother_gene == 1 and father_gene == 1:
            probability = 0.5 * 0.5
        
        elif (mother_gene == 1 and father_gene == 0) or (father_gene == 1 and mother_gene == 0):
            probability = 0.5 * (1 - mutation)
            
        elif (mother_gene == 2 and father_gene == 0) or (father_gene == 2 and mother_gene == 0):
            probability = mutation * (1 - mutation)
            
        elif mother_gene == 0 and father_gene == 0:
            probability = (1 - mutation) * (1 - mutation)

    # calculate the probability that child has 1 gene:        
    elif child_gene == 1:
        # If child_gene = 1, then mother's gene passed and father's gene did not pass 
        # OR mother's gene did not pass and father's gene passed

        # If gene = 2, then it can pass and not mutate or it can not pass and mutate
        # If gene = 1, then it can pass with probability 50% or not pass with probability 50%
        # If gene = 0, then it can pass and mutate, or it can not pass and not mutate
            
        if mother_gene == 2 and father_gene == 2:
            probability = (1 - mutation) * mutation + mutation * (1-mutation)

        elif (mother_gene == 2 and father_gene == 1) or (father_gene == 2 and mother_gene == 1):
            probability = (1 - mutation) * 0.5 + 0.5 * mutation
            
        elif mother_gene == 1 and father_gene == 1:
            probability = 0.5 * 0.5 + 0.5 * 0.5
            
        elif (mother_gene == 1 and father_gene == 0) or (father_gene == 1 and mother_gene == 0):
            probability = 0.5 * (1 - mutation) + 0.5 * mutation
            
        elif (mother_gene == 2 and father_gene == 0) or (father_gene == 2 and mother_gene == 0):
            probability = (1-mutation) * (1-mutation) + mutation * mutation
            
        elif mother_gene == 0 and father_gene == 0:
            probability = (1 - mutation) * mutation + mutation * (1 - mutation)
        
    elif child_gene == 2:
        # if child gene = 2, then both genes of parents passed

        # If gene = 2, then it did not mutate and passed
        # If gene = 1, then it can pass with probability 50%
        # If gene = 0, then it can pass and mutate

        if mother_gene == 2 and father_gene == 2:
            probability = (1 - mutation) * (1 - mutation)

        elif (mother_gene == 2 and father_gene == 1) or (father_gene == 2 and mother_gene == 1):
            probability = (1 - mutation) * 0.5
            
        elif mother_gene == 1 and father_gene == 1:
            probability = 0.5 * 0.5
            
        elif (mother_gene == 1 and father_gene == 0) or (father_gene == 1 and mother_gene == 0):
            probability = 0.5 * mutation
            
        elif (mother_gene == 2 and father_gene == 0) or (father_gene == 2 and mother_gene == 0):
            probability = (1 - mutation) * mutation
            
        elif mother_gene == 0 and father_gene == 0:
            probability = mutation * mutation
        
    return probability


def get_probability_of_person_has_gene(people, person, gene, one_gene, two_genes, zero_genes):
    # does this person is dependent variable ? -> does this person have father or mother?
    probability_of_person_has_certain_gene = 1
    mother = people[person]["mother"]
    father = people[person]["father"]
    if mother or father:
        # according bayesian network probability_of_person_has_certain_gene = 
        # = P(person = gene | mother(person) = motherGene, father(person) = fatherGene)

        if mother in zero_genes:
            mother_gene = 0
        elif mother in one_gene:
            mother_gene = 1
        elif mother in two_genes:
            mother_gene = 2
        else:
            mother_gene = None
        
        if father in zero_genes:
            father_gene = 0
        elif father in one_gene:
            father_gene = 1
        elif father in two_genes:
            father_gene = 2
        else:
            father_gene = None
        
        # get P(person = gene | mother(person) = motherGene, father(person) = fatherGene)
        probability_of_person_has_certain_gene = get_joint_child_gene_probability_by_mother_father(
            mother_gene=mother_gene, father_gene=father_gene, child_gene=gene, mutation=PROBS['mutation'])

    # our data does not contain information about person's father or mother,
    # so according bayesian network it is independent variable,
    # thus probability of this is not dependent on other variables
    else:
        probability_of_person_has_certain_gene = PROBS['gene'][gene]
    
    return probability_of_person_has_certain_gene


def get_probability_of_person_has_trait(people, person, trait, zero_genes, one_gene, two_genes):

    if person in zero_genes:
        person_gene = 0
    elif person in one_gene:
        person_gene = 1
    elif person in two_genes:
        person_gene = 2
    else:
        person_gene = None
    
    return PROBS["trait"][person_gene][trait]


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """

    for person in probabilities:
        if person in one_gene:
            probabilities[person]["gene"][1] += p
        
        if person in two_genes:
            probabilities[person]["gene"][2] += p

        if person not in one_gene and person not in two_genes:
            probabilities[person]["gene"][0] += p
        
        if person in have_trait:
            probabilities[person]["trait"][True] += p
        
        if person not in have_trait:
            probabilities[person]["trait"][False] += p


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """

    for person in probabilities:
        # Normalize genes probability distribution
        gene_0 = probabilities[person]["gene"][0]
        gene_1 = probabilities[person]["gene"][1]
        gene_2 = probabilities[person]["gene"][2]

        all_genes = gene_0 + gene_1 + gene_2

        if all_genes != 0:
            probabilities[person]["gene"][0] = gene_0/all_genes
            probabilities[person]["gene"][1] = gene_1/all_genes
            probabilities[person]["gene"][2] = gene_2/all_genes

        # Normalize traits probability distribution
        trait_yes = probabilities[person]["trait"][True]
        trait_no = probabilities[person]["trait"][False]

        all_traits = trait_yes + trait_no

        if all_traits != 0:
            probabilities[person]["trait"][True] = trait_yes/all_traits
            probabilities[person]["trait"][False] = trait_no/all_traits


if __name__ == "__main__":
    main()