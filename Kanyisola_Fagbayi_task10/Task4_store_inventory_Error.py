
# Using TRY-EXCEPT for IndexErrors and TRY-EXCEPT-FINALLY
# Create a dictionary called store
store = {'candles': 30, 'bottle of fruit wine': 150, 'birthday cards': 150, 'boxes of tea': 18}
items = store.keys()
items_qty = store.values()

try:
    print(store["beans"])
except KeyError:
    print("\nOut of index range\n")

while True:
    print(store)
    order = input(f"\nWe currenlty have various items for sale, please enter your order: ")
    if order in items:
        print(f"\n{order} are available")
        quantity= int(input("\nPlease enter the quantity: "))
        order_update = store.copy()
        try:
            if quantity > order_update[order]:
                raise ValueError("\nQuantity not available")
            order_update[order] -= quantity
        except ValueError as e:
            print("\nError message:", e)
        except Exception as e:
            print("\nError message:", e)
        finally:
            print("\nSession closed.")





