import timeit
import cProfile
import copy

class Equal_Chocolates:
    def __init__(self):
        self.num_cases = int(input())
        self.test_cases = [[None for x in range(2)] for x in range(self.num_cases)]

        for i in range(self.num_cases):
            self.test_cases[i][0] = int(input())
            self.test_cases[i][1] = [int(x) for x in input().split()]

    def equalize(self, n, state):
        iteration = 0
        
        while True:
            state.sort()
            diff = state[-1] - state[0]

            if diff == 0:
                return iteration

            inc = 0
            if diff >= 5:
                inc = 5
            elif diff >= 2:
                inc = 2
            elif diff >= 1:
                inc = 1

            for i in range(n-1):
                state[i] += inc
            iteration += 1

    def main(self):
        test_cases_copy = copy.deepcopy(self.test_cases)
        for i in range(self.num_cases):
            print(self.equalize(test_cases_copy[i][0], test_cases_copy[i][1]))
    
ec = Equal_Chocolates()
#ec.main()
#bench=timeit.timeit(ec.main, number=3)
#print("****************************************") 
#print("%.2f " % bench)

cProfile.run('ec.main()')
