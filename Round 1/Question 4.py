import sys

def main():
    qty = None
    cost = None

    def fetch_quantity():
        try:
            """
            Returns a number, any number
            """
            ...
        except Exception:
            print("Something is wrong")
            sys.exit(1)
        return ...
        
    def fetch_cost():
        try:
            """
            Returns a number, any number
            """
            ...
        except:
            pass
        return ...

    def compute_cost_per_quantity():

        qty = fetch_quantity()
        cost = fetch_cost()
        try:
            cost_per_quantity = cost/qty
        except Exception:
            print("Something is wrong")
            sys.exit(1)
        return cost_per_quantity
        
    cost_per_quantity = compute_cost_per_quantity()
    a = 1 + 2 + cost_per_quantity
    b = 4 + 5
    print(a+b)
