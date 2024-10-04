# Sentence Parser

This project implements a simple natural language parser using context-free grammar (CFG) to analyze sentences and identify noun phrase chunks. The grammar and vocabulary are defined to recognize basic sentence structures and generate parse trees.

## Project Structure

- **`parser.py`**: This is the main Python script that defines the context-free grammar, parses the input sentences, and identifies noun phrase (NP) chunks. The key functions include:
  - **`preprocess(sentence)`**: Pre-processes the sentence by tokenizing, converting it to lowercase, and removing non-alphabetic words.
  - **`np_chunk(tree)`**: Extracts noun phrase chunks from the parsed sentence tree.
  - **`main()`**: The main function that handles file input or manual input, parses the sentence, and prints the parse tree and noun phrase chunks.

## How It Works

1. **Grammar Definition**: The grammar is defined using two parts:
   - **Terminals**: This includes part-of-speech (POS) tags such as adjectives, nouns, verbs, and more.
   - **Non-Terminals**: These are higher-level structures such as sentences (S), noun phrases (NP), and verb phrases (VP).
   
2. **Parsing**: The script uses the grammar and `nltk.ChartParser` to parse sentences into syntax trees. It can handle both single and compound sentences with conjunctions.

3. **Noun Phrase Chunks**: The parser identifies noun phrase chunks, which are subtrees labeled as NP but do not contain other noun phrases within them.

## Usage

To run the parser, use the following command:

```bash
python parser.py [filename]
```

- If a file is provided, the script will read the sentence from the file.
- If no file is provided, the script will prompt you to enter a sentence.

### Example

```bash
python parser.py
```

Input:
```
Sentence: Holmes smiled and sat in the armchair.
```

Output:
```
                  S                    
        __________|__________          
       |                     VP       
       |         _____________|___     
       NP       |                 VP  
  _____|____    |              ____|__ 
 N         V    V             P       NP
 |         |    |             |    ___|____
holmes   smiled and          sat  in the armchair

Noun Phrase Chunks
holmes
the armchair
```

## Requirements

- `nltk` library

To install `nltk`, run:
```bash
pip install nltk
```

Additionally, the script will download the `punkt` tokenizer from `nltk`, which is required for sentence tokenization.

## Grammar Details

The project uses a small set of terminals and non-terminals to define basic sentences. You can modify the `TERMINALS` and `NONTERMINALS` variables to adapt the parser to different vocabularies or more complex sentence structures.

### Terminals
The set of terminal symbols includes common adjectives, adverbs, conjunctions, determiners, nouns, prepositions, and verbs. For example:
- **Nouns (N)**: "holmes", "armchair", "door", "smile", "we", etc.
- **Verbs (V)**: "arrived", "came", "smiled", "sat", etc.

### Non-Terminals
The non-terminals define higher-level structures:
- **S**: Sentence
- **NP**: Noun Phrase
- **VP**: Verb Phrase

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests to enhance the project.