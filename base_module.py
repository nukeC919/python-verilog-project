import os

class BaseModule:
    def __init__(self, moduleName):
        self.moduleName = moduleName
        self.results = ""
    
    def makeTestbench(self):
        print("<Verilog>  Generating testbench...")
    
    def simulate(self):
        print("<Verilog>  Simulating file...")
        os.system(f"iverilog -o result {self.moduleName}.v {self.moduleName}_tb.v")
    
    def getResults(self, deleteFiles=False):
        print("<Verilog>  Get results...")
        self.results = os.popen("vvp result").readlines()
        if deleteFiles:
            os.system(f"del {self.moduleName}_tb.v")
            os.system(f"del result")
    
    def parseResults(self):
        print("<Verilog>  Parsing results...")