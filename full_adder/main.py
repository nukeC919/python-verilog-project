from full_adder import FullAdder

def input01(var):
    v = input(f"->  {var:3s} = ")
    while v not in ["0", "1"] :
        print("[Warning] The input is not 0 or 1.")
        v = input(f"->  {var:3s} = ")
    return int(v)


print("[ Full Adder ]")
print("Please input a, b, cin (value: 0, 1)")
a, b, cin = 0, 0, 0
a = input01("a")
b = input01("b")
cin = input01("cin")

FA = FullAdder(a, b, cin)
FA.run()