# By importing the system we are using data stores in another data region
# Metadata importing the sephora_system
import sephora_system as gs

user_shopping = True

print ("\nWelcome to the Sephora store")
print("You can get all kinds of makeup, skincare and hair products here!")
print("What would you like to buy today?")
print()

while user_shopping:
    print("Options: \n")
    print("Add to Cart: \n")
    print("Benefit Brow Gel (1) | Tarte Concealer (2) | Maybelline Foundation (3) | Olaplex Shampoo (4) | Loreal Mascara (5) | Clinique Cleanser (6)")
    print("\nCheck count of:\n ")
    print("Benefit Brow Gel(1a) | Tarte Concealer (2a) | Maybelline Foundation count (3a) | Olaplex Shampoo (4a) | Loreal Mascara (5a) | Clinique Cleanser (6a)")
    print("\nRemove: \n")
    print("Benefit Brow Gel(1b) | Tarte Concealer (2b) | Maybelline Foundation count (3b) | Olaplex Shampoo (4b) | Loreal Mascara (5b) | Clinique Cleanser (6b)")
    print("\nRead instructions: \n")
    print("Benefit Brow Gel(1c) | Tarte Concealer (2c) | Maybelline Foundation count (3c) | Olaplex Shampoo (4c) | Loreal Mascara (5c) | Clinique Cleanser (6c)")
    print("\nAdd product to shelf: \n")
    print("Product 1 (1d) | Product 2 (2d) | Product 3 (3d) | Product 4 (4d) | Product 5 (5d) | Product 6 (6d)")
    print("\nRemove products from shelf: \n")
    print("Product 1 (1e) | Product 2 (2e) | Product 3 (3e) | Product 4 (4e) | Product 5 (5e) | Product 6 (6e)")
    print("\nLeave store (e)\n")
    user_input = input("What would you like to do: ")
    print(user_input)
    if user_input == '1':
        gs.buy_benefit_brow_gel()
    elif user_input == '1a':
        print(gs.benefit_brow_count)
    elif user_input == '1b':
        gs.remove_benefit_brow_gel()
        print("Product removed.")
    elif user_input == '1c':
        print(gs.read_instructions_benefit_brow())
    elif user_input == '1d':
        gs.stock_new_product()
        print(gs.stock_new_product)
    elif user_input == '1e':
        gs.remove_new_product()
        print("Product removed.")
    elif user_input == '2':
        gs.buy_tarte_concealer()
    elif user_input == '2a':
        print(gs.tarte_concealer_count)
    elif user_input == '2b':
        gs.remove_tarte_concealer()
        print("Product removed.")
    elif user_input == '2c':
        print(gs.read_instructions_tarte_concealer())
    elif user_input == '2d':
        gs.stock_new_product_1()
        print(gs.stock_new_product_1())
    elif user_input == '2e':
        gs.remove_new_product_1()
        print("Product removed.")
    elif user_input == '3':
        gs.buy_maybelline_foundation()
    elif user_input == '3a':
        print(gs.maybelline_foundation_count)
    elif user_input == '3b':
        gs.remove_maybelline_foundation()
        print("Product removed.")
    elif user_input == '3c':
        print(gs.read_instructions_maybelline_foundation())
    elif user_input == '3d':
        gs.stock_new_product_2()
        print(gs.stock_new_product_2())
    elif user_input == '3e':
        gs.remove_new_product_2()
        print("Product removed.")
    elif user_input == '4':
        gs.buy_olaplex_shampoo()
    elif user_input == '4a':
        print(gs.olaplex_shampoo_count)
    elif user_input == '4b':
        gs.remove_olaplex_shampoo()
        print("Product removed.")
    elif user_input == '4c':
        print(gs.read_instructions_olaplex_shampoo())
    elif user_input == '4d':
        gs.stock_new_product_3()
        print(gs.stock_new_product)
    elif user_input == '4e':
        gs.remove_new_product_3()
        print("Product removed.")
    elif user_input == '5':
        gs.buy_loreal_mascara()
    elif user_input == '5a':
        print(gs.loreal_mascara_count)
    elif user_input == '5b':
        gs.remove_loreal_mascara()
        print("Product removed.")
    elif user_input == '5c':
        print(gs.read_instructions_loreal_mascara())
    elif user_input == '5d':
        gs.stock_new_product_4()
        print(gs.stock_new_product_4())
    elif user_input == '1e':
        gs.remove_new_product_4()
        print("Product removed.")
    elif user_input == '6':
        gs.buy_clinique_cleanser()
    elif user_input == '6a':
        print(gs.clinique_cleanser_count)
    elif user_input == '6b':
        gs.remove_clinique_cleanser()
        print("Product removed.")
    elif user_input == '6c':
        print(gs.read_instructions_clinique_cleanser())
    elif user_input == '6d':
        gs.stock_new_product_5()
        print(gs.stock_new_product_5())
    elif user_input == '6e':
        gs.remove_new_product_5()
        print("Product removed.")
    elif user_input == 'e':
        print("Goodbye!")
        break

