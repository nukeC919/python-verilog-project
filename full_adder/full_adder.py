import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from base_module import BaseModule

class FullAdder(BaseModule):
    def __init__(self, a, b, cin):
        super().__init__(moduleName="full_adder")
        self.a = a
        self.b = b
        self.cin = cin
        self.s = 0
        self.cout = 0
    
    
    def run(self):
        self.makeTestbench()
        super().simulate()
        super().getResults(deleteFiles=True)
        self.parseResults()
        self.printIO()
    
    
    def makeTestbench(self):
        super().makeTestbench()
        f = open(f"{self.moduleName}_tb.v", 'w')
        
        f.write(f"module {self.moduleName}_tb;                         \n")
        f.write( "    reg a, b, cin;                                   \n")
        f.write( "    wire s, cout;                                    \n")
        f.write( "        full_adder FA(a, b, cin, s, cout);           \n")
        f.write( "    initial begin                                    \n")
        f.write( "    $monitor(\"%b %b\",s,cout);                      \n")
        f.write(f"        a = {self.a}; b = {self.b}; cin = {self.cin};\n")
        f.write( "    end                                              \n")
        f.write( "endmodule                                              ")
        f.close()
    
    
    def parseResults(self):
        super().parseResults()
        res = self.results[0].rstrip()
        self.s, self.cout = map(int, res.split())
    
    
    def printIO(self):
        print(f"[ Inputs ]     a         | {self.a}")
        print(f"               b         | {self.b}")
        print(f"               c in      | {self.cin}")
        print( "-----------------------------")
        print(f"[ Outputs ]    sum       | {self.s}")
        print(f"               carry out | {self.cout}")