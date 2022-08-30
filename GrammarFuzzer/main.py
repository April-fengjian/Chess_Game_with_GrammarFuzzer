from fuzzingbook.GeneratorGrammarFuzzer import GeneratorGrammarFuzzer, CHARGE_GRAMMAR
from fuzzingbook.GrammarFuzzer import GrammarFuzzer, display_tree
from fuzzingbook.Grammars import *
import copy
import string

Grammar = Dict[str, List]
Command_Grammar = {
    "<start>": ["<command>"],
    "<command>": ["<players>\n<player-move>"],
    # "<operation>": ["undo"],
    "<players>": ["<player>\n<player>"],
    "<player>": ["human", "computer[1]", "computer[2]", "computer[3]", "computer[4]"],
    "<player-move>": ["move\n", "move <Position> <Position>\n","<player-move><player-move>"],
    "<Position>": ["<column><row>"],
    "<column>": srange(string.ascii_letters)[:8],
    "<row>": crange('1', '8'),
}
Grammar_hc = {
    "<start>": ["<command>"],
    "<command>": ["<players>\n<move>"],
    "<players>": ["<player1>\n<player2>"],
    "<player1>": ["human"],
    "<player2>": ["computer[1]", "computer[2]", "computer[3]", "computer[4]"],
    "<move>": ["<player-move><computer-move>"],
    # "<operation>": ["resign", "undo", "history", "standardopening"],
    "<computer-move>": ["move\n","move\n<move><move>"],
    "<player-move>": ["move <Position> <Position>\n"],
    "<Position>": ["<column><row>"],
    "<column>": srange(string.ascii_letters)[:8],
    "<row>": crange('1', '8'),
}
Grammar_cc = {
    "<start>": ["<command>"],
    "<command>": ["<players>\n<move>"],
    "<players>": ["<player>\n<player>"],
    "<player>": ["computer[1]", "computer[2]", "computer[3]", "computer[4]"],
    "<move>": ["move\n", "<move><move>","move\n"],
}
Grammar_hh = {
    "<start>": ["<command>"],
    "<command>": ["<players>\n<player-move>"],
    "<players>": ["<player>\n<player>"],
    "<player>": ["human"],
    # "<move>": ["<player-move>\n<player-move>"],
    "<player-move>": ["move <Position> <Position>\n","<player-move><player-move>","move <Position> <Position>\n"],
    # "<operation>": ["resign", "undo", "history", "standardopening"],
    "<Position>": ["<column><row>"],
    "<column>": srange(string.ascii_letters)[:8],
    "<row>": crange('1', '8'),
}

assert is_valid_grammar(Command_Grammar)


def srange(characters: str) -> List[Expansion]:
    """Construct a list with all characters in the string"""
    return [c for c in characters]


def crange(character_start: str, character_end: str) -> List[Expansion]:
    return [chr(i)
            for i in range(ord(character_start), ord(character_end) + 1)]


def simple_grammar_fuzzer(grammar: Grammar,
                          start_symbol: str = START_SYMBOL,
                          max_nonterminals: int = 50,
                          max_expansion_trials: int = 100,
                          log: bool = False) -> str:
    """Produce a string from `grammar`.
           `start_symbol`: use a start symbol other than `<start>` (default).
           `max_nonterminals`: the maximum number of nonterminals
             still left for expansion
           `max_expansion_trials`: maximum # of attempts to produce a string
           `log`: print expansion progress if True"""
    term = start_symbol
    expansion_trials = 0
    while len(nonterminals(term)) > 0:
        symbol_to_expand = random.choice(nonterminals(term))
        expansions = grammar[symbol_to_expand]
        expansion = random.choice(expansions)
        # In later chapters, we allow expansions to be tuples,
        # with the expansion being the first element
        if isinstance(expansion, tuple):
            expansion = expansion[0]
        new_term = term.replace(symbol_to_expand, expansion, 1)
        if len(nonterminals(new_term)) < max_nonterminals:
            term = new_term
            if log:
                print("%-40s" % (symbol_to_expand + " -> " + expansion), term)
            expansion_trials = 0
        else:
            expansion_trials += 1
            if expansion_trials >= max_expansion_trials:
                raise ExpansionError("Cannot expand " + repr(term))
    return term

file = open('fuzzCommands.txt','w')
for i in range(50):
     fc = simple_grammar_fuzzer(grammar=Command_Grammar)
     print(fc)
     file.write(fc)
     file.write("END\n")
     print("--------------------------------------")
     fc = simple_grammar_fuzzer(grammar=Grammar_hc)
     print(fc)
     file.write(fc)
     file.write("END\n")
     print("--------------------------------------")
     fc = simple_grammar_fuzzer(grammar=Grammar_cc)
     print(fc)
     file.write(fc)
     file.write("END\n")
     print("--------------------------------------")
    fc = simple_grammar_fuzzer(grammar=Grammar_hh)
    print(fc)
    file.write(fc)
    file.write("END\n")
    print("--------------------------------------")

