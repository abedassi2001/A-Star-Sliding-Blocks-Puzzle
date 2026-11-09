import time

from search import search, get_gen_exp_count
from heuristics import *
from flat_board_state import *



if __name__ == '__main__':

    board = [[3, 3, 0], [2, 2, 1], [0,1,1]]

    start_state = flat_board_state(board)

    start_time = time.time()
    search_result = search(start_state, base_heuristic)
    end_time = time.time() - start_time

    print(end_time)
    # solution cost
    print(search_result[-1].g)
    print(get_gen_exp_count())