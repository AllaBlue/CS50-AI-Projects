import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("crossword/assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """

        # For every variable in domains if any value in the variable domain
        # does not have the same length as variable, we will remove this 
        # value from the variable domain
        for variable in self.domains:
            domain = self.domains[variable].copy()
            for word in domain:
                if variable.length != len(word):
                    self.domains[variable].remove(word)
        
    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        # We did not change domain
        revised = False
        
        domain = self.domains[x].copy()
        # For every value in the variable X domain
        for word_x in domain:
            satisfy = []
            # if X and Y are neighbors (means overlaps)
            if self.crossword.overlaps[x, y] != None:
                # get the point of intersection
                (i, j) = self.crossword.overlaps[x, y]
                # Check if considered value from domain X satisfies the binary 
                # condition for every value in domain Y
                for word_y in self.domains[y]:
                    if word_x[i] != word_y[j]:
                        satisfy.append(False)
                    else:
                        satisfy.append(True)
            else:
                satisfy.append(True)
            
            # if value from domain X does not satisfy the binary condition with any value from domain Y
            # we will remove this value from the X domain
            if not any(satisfy):
                self.domains[x].remove(word_x)
                revised = True
        
        # We changed domain X
        return revised

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """

        # If arcs is not provided we will create a queue of all arcs in the crossword problem
        if arcs == None:
            queue = set()
            for variable1 in self.domains:
                for variable2 in self.domains:
                    if variable1 == variable2:
                        continue

                    queue.add((variable1, variable2))
        else:
            queue = arcs
        
        # While queue is not empty - while there is at least one pair of variables to consider
        while len(queue) != 0:
            # get this pair of variables
            (x, y) = queue.pop()

            # Cehck if values from X domain satisfy binary condition with values from Y domain
            if self.revise(x, y):

                # If there is no value in domain X that satisfies condition,
                # there is no solution to the problem
                if len(self.domains[x]) == 0:
                    return False
                
                for z in self.crossword.neighbors(x).difference({y}):
                    queue.add((z, x))
        
        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        
        # Check if all variables are present in assignment and if they are assigned.
        for variable in self.domains:
            if variable not in assignment:
                return False
            elif not assignment[variable]:
                return False
        
        return True

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        
        for variable1, value1 in assignment.items():
            for variable2, value2 in assignment.items():

                # Check if all values are distinct -> one value can be assigned only to one variable
                if variable1 != variable2 and value1 == value2:
                    return False
                
                # Check if there are no conflicts between neighboring variables
                if variable2 in self.crossword.neighbors(variable1):
                    (i, j) = self.crossword.overlaps[variable1, variable2]
                    if value1[i] != value2[j]:
                        return False
            
            # Check if every value is the correct length
            if variable1.length != len(value1):
                return False
        
        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        rule_out = []
        # For every value in the variable var domain
        for val in self.domains[var]:
            
            count = 0
            # If value is already in the assignment, do not consider this value
            if val in assignment.values():
                continue

            # For every other variable in domains
            for var2 in self.domains:
                if var2 in assignment or var2 == var:
                    continue

                # For every value in the other variable domain if values are equal,
                # increase the rule_out of value of this value.
                for val2 in self.domains[var2]:
                    if val == val2:
                        count += 1

            rule_out.append((val, count))
        
        sorted_rule_out = sorted(rule_out, key=lambda x: x[1])
        result = list(value[0] for value in sorted_rule_out)

        return result

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """

        # Create list of dictinaries that maps each variable to it domain length and degree
        variables = []
        for variable in self.domains:
            if variable not in assignment:
                variables.append({"variable": variable, 
                                  "domain_length": len(self.domains[variable]),
                                  "degree": len(self.crossword.neighbors(variable))})
        
        # return sorted list of variables by th least domain length and the highest degree
        return sorted(variables, key=lambda var: (var["domain_length"], -var["degree"]))[0]["variable"]

    def get_inferences(self):
        # Create dictionary of inferences that we get after running ac3
        # If the variable has in it's domain only one value, then assign to this variable this value
        inferences = {}
        for variable, value in self.domains.items():
            if len(value) == 1:
                inferences[variable] = value.copy().pop()
        
        return inferences

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        # If assignment is complete we return the assignment - solution to the problem
        if self.assignment_complete(assignment=assignment):
            return assignment
        
        try:
            # Select unassigned variable from the domains of variables
            variable = self.select_unassigned_variable(assignment=assignment)
            # Sort domain values of this variable by least constrainig values algorithm
            domain = self.order_domain_values(var=variable, assignment=assignment)

            for value in domain:
                new_assignment = assignment.copy()
                # Try to assign the first value to this variable
                new_assignment[variable] = value

                # If assignment consistent (no problem) then assign this value to the variable
                if self.consistent(assignment=new_assignment):
                    assignment[variable] = value

                    # check for the binary conditions
                    ac3 = self.ac3()

                    # get inferences and update assignment with these inferences
                    if ac3:
                        inferences = self.get_inferences()
                        assignment.update(inferences)
                    
                    # Again run backtrack with new assignment
                    result = self.backtrack(assignment=assignment)

                    # If no failure return solution
                    if result:
                        return result
                    
                    # If was failure remove inferences from the assignment 
                    # and remove the last assigned value to the variable.
                    # Try to assign another value from the list of values in sorted domain of the variable
                    assignment.pop(variable)
                    for var in inferences.keys():
                        assignment.pop(var)
        except Exception:
            return None
        
        return None
    

def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python crossword/generate.py crossword/data/structure crossword/data/words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()