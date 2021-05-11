from functions import *
import timeit


def main():
    tic_tac_toe_tree = make_tree()
    minimax_search_depth1 = 2
    minimax_search_depth2 = 4
    minimax_search_depth3 = 6
    minimax_search_depth4 = 10
    x = []
    o = []
    d = []
    for i in range(6):
        x.append(0)
        o.append(0)
        d.append(0)
    for i in range(1000):
        games = []
        print("Random game result:\n")
        games.append(random_game(tic_tac_toe_tree))
        print(games[0])
        print("MinimaxFull game result:\n")
        games.append(minimax_full_game(tic_tac_toe_tree))
        print(games[1])
        print(f"Minimax with search depth = {minimax_search_depth1} game result:\n")
        games.append(minimax_game(tic_tac_toe_tree, minimax_search_depth1))
        print(games[2])
        print(f"Minimax with search depth = {minimax_search_depth2} game result:\n")
        games.append(minimax_game(tic_tac_toe_tree, minimax_search_depth2))
        print(games[3])
        print(f"Minimax with search depth = {minimax_search_depth3} game result:\n")
        games.append(minimax_game(tic_tac_toe_tree, minimax_search_depth3))
        print(games[4])
        print(f"Minimax with search depth = {minimax_search_depth4} game result:\n")
        games.append(minimax_game(tic_tac_toe_tree, minimax_search_depth4))
        print(games[5])
        for j in range(len(games)):
            if games[j] == 1:
                x[j] += 1
            elif games[j] == -1:
                o[j] += 1
            elif games[j] == 0:
                d[j] += 1
        print(24 * '-')
    print("Random games: x wins: " + str(x[0]) + ", o wins: " + str(o[0]) + ", draws: " + str(d[0]))
    print("MinimaxFull games: x wins: " + str(x[1]) + ", o wins: " + str(o[1]) + ", draws: " + str(d[1]))
    print(f"Minimax with search depth = {minimax_search_depth1} games: x wins: " + str(x[2]) + ", o wins: " + str(
        o[2]) + ", draws: " + str(d[2]))
    print(f"Minimax with search depth = {minimax_search_depth2} games: x wins: " + str(x[3]) + ", o wins: " + str(
        o[3]) + ", draws: " + str(d[3]))
    print(f"Minimax with search depth = {minimax_search_depth3} games: x wins: " + str(x[4]) + ", o wins: " + str(
        o[4]) + ", draws: " + str(d[4]))
    print(f"Minimax with search depth = {minimax_search_depth4} games: x wins: " + str(x[5]) + ", o wins: " + str(
        o[5]) + ", draws: " + str(d[5]))

    random = 0
    min_full = 0
    min_d2 = 0
    min_d4 = 0
    min_d6 = 0
    min_d10 = 0
    for i in range(10):
        random += timeit.timeit(lambda: random_game(tic_tac_toe_tree), number=1)
        min_full += timeit.timeit(lambda: minimax_full_game(tic_tac_toe_tree), number=1)
        min_d2 += timeit.timeit(lambda: minimax_game(tic_tac_toe_tree, minimax_search_depth1), number=1)
        min_d4 += timeit.timeit(lambda: minimax_game(tic_tac_toe_tree, minimax_search_depth2), number=1)
        min_d6 += timeit.timeit(lambda: minimax_game(tic_tac_toe_tree, minimax_search_depth3), number=1)
        min_d10 += timeit.timeit(lambda: minimax_game(tic_tac_toe_tree, minimax_search_depth4), number=1)

    print(f"Execution time for random game: {random/10:.2f} seconds")
    print(f"Execution time for MinimaxFull game: {min_full/10:.2f} seconds")
    print(f"Execution time for Minimax with search depth = {minimax_search_depth1} game: {min_d2/10:.2f} seconds")
    print(f"Execution time for Minimax with search depth = {minimax_search_depth2} game: {min_d4/10:.2f} seconds")
    print(f"Execution time for Minimax with search depth = {minimax_search_depth3} game: {min_d6/10:.2f} seconds")
    print(f"Execution time for Minimax with search depth = {minimax_search_depth4} game: {min_d10/10:.2f} seconds")


if __name__ == '__main__':
    main()
