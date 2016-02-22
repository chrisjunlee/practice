import pdb
import bcolors

class ABC:
    def max(self, a, b, c):
        return a*(b + c) + b*c

    def createString(self, N, K):
        if N**2/3 < K:
            return ""

        split_result = self.changify(N//3, N//3, K)
        a_splits = split_result[0]
        b_splits = self.changify(N//3, N//3, split_result[1])[0]

        str1 = ''
        c_count = 0
        if b_splits:
            for b in b_splits:
                if c_count < b:
                    for i in range(b - c_count):
                        str1 += 'C'
                        c_count += 1
                str1 += 'B'

        c_count = len(str1)
        if a_splits:
            for a in a_splits:
                if c_count < a:
                    for i in range(a - c_count):
                        str1 += 'C'
                        c_count += 1
                str1 += 'A'

        # filling remaining space with 'C'
        for i in range(N - len(str1)):
            str1 += 'C'
        return str1[::-1]
        
    def changify(self, max_splits, denom, amount):
        splits = [None for i in range(max_splits)]
        remainder = amount
        for i in range(max_splits):
            if remainder >= denom:
                splits[i] = denom
                remainder -= denom
            elif remainder > 0:
                splits[i] = remainder
                remainder = 0
                break

        while splits and splits[-1] is None:
            splits.pop()
        splits.reverse()
        return (splits, remainder)

    def compute_value(self, str1):
        b, c, sum1 = 0, 0, 0
        for s in reversed(str1):
            if s == 'C':
                c += 1
            elif s == 'B':
                b += 1
                sum1 += c
            else:
                sum1 += b + c
        return sum1
                
    def test(self, N, K, expected):
        cst = self.createString(N, K)
        print("****************************************")
        print("Test N:%2d K:%2d %s" % (N, K, cst))
        if cst == expected:
            print(bcolors.OKGREEN + "\tPass" + bcolors.ENDC)
        else:
            print(bcolors.FAIL + "  Expected: " + expected)
            print("  Acutal:   %s %d %s" % (cst, self.compute_value(cst), bcolors.ENDC))
        print("")

abc = ABC()
#abc.test(3, 0, "CCC")
#abc.test(3, 3, "ABC")
abc.test(15,30,"CCCCAAAAABCCCCC")
#str1 = "CABBACCBAABCBBB"
#str2 = "CCAAAACCCCACCCC"
#print(str1 + ": %d" % abc.compute_value(str1))
#print(str2 + ": %d" % abc.compute_value(str2))

#print(str(abc.changify(4, 9, 30)))

#cst = abc.createString(15,30)
#print(cst)
#print(str(abc.compute_value(cst)))
