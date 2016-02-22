class Bullets:
    def match(self, guns, bullet):
        matched = False
        i = 0
        for gun in guns:
            if self.cyclicEqual(gun, bullet):
                return i
            else:
                i += 1
        return -1
            
    def cyclicEqual(self, st1, st2):
        for i in range(len(st1)):
            if (st1[i:] + st1[:i] == st2):
                return True
        return False
    
b = Bullets()
guns = {"| | | |","|| || |"," ||||  "}
bullet = "|| || |"
print(b.match(guns,bullet))
