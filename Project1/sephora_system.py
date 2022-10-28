# Sephora SYSTEM
benefit_brow_count = 20
tarte_concealer_count = 20
maybelline_foundation_count = 20
olaplex_shampoo_count = 20
loreal_mascara_count = 20
clinique_cleanser_count = 20
soldout_product = ["Olaplex Conditioner", "MAC Rouge Lipstick"]

file = ["" for item in range(12)]

# Data bitmap containing the index
bitmap_block = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]

# Inode bitmap containing instructions for the products
file[0] = "Brush it on your brows"
file[1] = "Apply on your blemishes"
file[2] = "Apply evenly on your face"
file[3] = "Lather on your scalp"
file[4] = "Brush it on your eyelashes"
file[5] = "Add water to wash your face"

# Inode table, Inode bitmap
# These inodes contain information that connects to the shelf items
inode1 = {"filename": "Benefit Brow", "location": 0, "expiration": "3/3/2025"}
inode2 = {"filename": "Tarte Concealer", "location": 1, "expiration": "6/3/2023"}
inode3 = {"filename": "Maybelline Foundation", "location": 2, "expiration": "10/1/2026"}
inode4 = {"filename": "Olaplex Shampoo", "location": 3, "expiration": "8/1/2024"}
inode5 = {"filename": "Loreal Mascara", "location": 4, "expiration": "3/6/2025"}
inode6 = {"filename": "Clinique Cleanser", "location": 5, "expiration": "1/3/2028"}
inode7 = {"filename": "", "location": "", "expiration": ""}
inode8 = {"filename": "", "location": "", "expiration": ""}
inode9 = {"filename": "", "location": "", "expiration": ""}
inode10 = {"filename": "", "location": "", "expiration": ""}
inode11 = {"filename": "", "location": "", "expiration": ""}
inode12 = {"filename": "", "location": "", "expiration": ""}


# This function prints out file name information listed on the inodes
def look_on_shelf():
    print(inode1["filename"])
    print(inode2["filename"])
    print(inode3["filename"])
    print(inode4["filename"])
    print(inode5["filename"])
    print(inode6["filename"])
    print(inode7["filename"])
    print(inode8["filename"])
    print(inode9["filename"])
    print(inode10["filename"])
    print(inode11["filename"])
    print(inode12["filename"])


# This function removes the shelf item using the pop function to set the data block in the index back to 0
def remove_benefit_brow_gel():
    file.pop(0)
    inode1["filename"] = ""
    inode1["location"] = ""
    inode1["expiration"] = ""
    bitmap_block[0] = 0


# This function removes the shelf item using the pop function to set the data block in the index back to 0
def remove_tarte_concealer():
    file.pop(1)
    inode2["filename"] = ""
    inode2["location"] = ""
    inode2["expiration"] = ""
    bitmap_block[1] = 0


# This function removes the shelf item using the pop function to set the data block in the index back to 0
def remove_maybelline_foundation():
    file.pop(2)
    inode3["filename"] = ""
    inode3["location"] = ""
    inode3["expiration"] = ""
    bitmap_block[2] = 0


# This function removes the shelf item using the pop function to set the data block in the index back to 0
def remove_olaplex_shampoo():
    file.pop(3)
    inode4["filename"] = ""
    inode4["location"] = ""
    inode4["expiration"] = ""
    bitmap_block[3] = 0


# This function removes the shelf item using the pop function to set the data block in the index back to 0
def remove_loreal_mascara():
    file.pop(4)
    inode5["filename"] = ""
    inode5["location"] = ""
    inode5["expiration"] = ""
    bitmap_block[4] = 0


# This function removes the shelf item using the pop function to set the data block in the index back to 0
def remove_clinique_cleanser():
    file.pop(5)
    inode6["filename"] = ""
    inode6["location"] = ""
    inode6["expiration"] = ""
    bitmap_block[5] = 0


# This function removes the shelf item using the pop function to set the data block in the index back to 0
def remove_new_product():
    file.pop(6)
    inode7["filename"] = ""
    inode7["location"] = ""
    inode7["expiration"] = ""
    bitmap_block[6] = 0


# This function removes the shelf item using the pop function to set the data block in the index back to 0
def remove_new_product_1():
    file.pop(7)
    inode8["filename"] = ""
    inode8["location"] = ""
    inode8["expiration"] = ""
    bitmap_block[7] = 0


# This function removes the shelf item using the pop function to set the data block in the index back to 0
def remove_new_product_2():
    file.pop(8)
    inode9["filename"] = ""
    inode9["location"] = ""
    inode9["expiration"] = ""
    bitmap_block[8] = 0


# This function removes the shelf item using the pop function to set the data block in the index back to 0
def remove_new_product_3():
    file.pop(9)
    inode10["filename"] = ""
    inode10["location"] = ""
    inode10["expiration"] = ""
    bitmap_block[9] = 0


# This function removes the shelf item using the pop function to set the data block in the index back to 0
def remove_new_product_4():
    file.pop(10)
    inode11["filename"] = ""
    inode11["location"] = ""
    inode11["expiration"] = ""
    bitmap_block[10] = 0


# This function removes the shelf item using the pop function to set the data block in the index back to 0
def remove_new_product_5():
    file.pop(11)
    inode12["filename"] = ""
    inode12["location"] = ""
    inode12["expiration"] = ""
    bitmap_block[11] = 0


# This function adds data blocks to the inode of the new items added on the shelf
def stock_new_product(product):
    for p in range(12):
        if file[p] == "":
            file[p] = "This is hazardous to eat"
            inode7["filename"] = product
            inode7["location"] = "6"
            inode7["expiration"] = "1/1/2030"


# This function adds data blocks to the inode of the new items added on the shelf
def stock_new_product_1(product):
    for p in range(12):
        if file[p] == "":
            file[p] = "This is hazardous to eat"
            inode8["filename"] = product
            inode8["location"] = "7"
            inode8["expiration"] = "1/1/2030"


# This function adds data blocks to the inode of the new items added on the shelf
def stock_new_product_2(product):
    for p in range(12):
        if file[p] == "":
            file[p] = "This is hazardous to eat"
            inode9["filename"] = product
            inode9["location"] = "8"
            inode9["expiration"] = "1/1/2030"


# This function adds data blocks to the inode of the new items added on the shelf
def stock_new_product_3(product):
    for p in range(12):
        if file[p] == "":
            file[p] = "This is hazardous to eat"
            inode10["filename"] = product
            inode10["location"] = "9"
            inode10["expiration"] = "1/1/2030"


# This function adds data blocks to the inode of the new items added on the shelf
def stock_new_product_4(product):
    for p in range(12):
        if file[p] == "":
            file[p] = "This is hazardous to eat"
            inode11["filename"] = product
            inode11["location"] = "10"
            inode11["expiration"] = "1/1/2030"


# This function adds data blocks to the inode of the new items added on the shelf
def stock_new_product_5(product):
    for p in range(12):
        if file[p] == "":
            file[p] = "This is hazardous to eat"
            inode12["filename"] = product
            inode12["location"] = "11"
            inode12["expiration"] = "1/1/2030"


# This function verifies the sold out products that are in the sold out products data bitmap index
def sold_out_product(product):
    if product in soldout_product:
        return True

# This function adds products that are not sold out to the shelf
def addto_sold_out_product(product):
    if not sold_out_product(product):
        soldout_product.append(product)
    else:
        print("This product is sold out")

# This function adds the product to the cart and removes the count from the shelf each time it is added to cart
def buy_benefit_brow_gel():
    global benefit_brow_count
    if benefit_brow_count > 0:
        benefit_brow_count -= 1
        print("Added Benefit Brow Gel to cart")
    else:
        print("There's no Benefit Brow Gel left.")

# This function adds the product to the cart and removes the count from the shelf each time it is added to cart
def buy_tarte_concealer():
    global tarte_concealer_count
    if tarte_concealer_count > 0:
        tarte_concealer_count -= 1
        print("Added Tarte Concealer to cart")
    else:
        print("There's no Tarte Concealer left.")

# This function adds the product to the cart and removes the count from the shelf each time it is added to cart
def buy_maybelline_foundation():
    global maybelline_foundation_count
    if maybelline_foundation_count > 0:
        maybelline_foundation_count -= 1
        print("Added Maybelline Foundation to cart")
    else:
        print("There's no Maybelline Foundation left.")

# This function adds the product to the cart and removes the count from the shelf each time it is added to cart
def buy_olaplex_shampoo():
    global olaplex_shampoo_count
    if olaplex_shampoo_count > 0:
        olaplex_shampoo_count -= 1
        print("Added Olaplex Shampoo to cart")
    else:
        print("There's no Olaplex Shampoo left.")

# This function adds the product to the cart and removes the count from the shelf each time it is added to cart
def buy_loreal_mascara():
    global loreal_mascara_count
    if loreal_mascara_count > 0:
        loreal_mascara_count -= 1
        print("Added Loreal Mascara to cart")
    else:
        print("There's no Loreal Mascara left.")

# This function adds the product to the cart and removes the count from the shelf each time it is added to cart
def buy_clinique_cleanser():
    global clinique_cleanser_count
    if clinique_cleanser_count > 0:
        clinique_cleanser_count -= 1
        print("Added Clinique Cleanser to cart")
    else:
        print("There's no Clinique Cleanser left.")


# These read instructions functions prints the instructions listed on the data index above where instructions are listed
def read_instructions_benefit_brow():
    print(file[0])


def read_instructions_tarte_concealer():
    print(file[1])


def read_instructions_maybelline_foundation():
    print(file[2])


def read_instructions_olaplex_shampoo():
    print(file[3])


def read_instructions_loreal_mascara():
    print(file[4])


def read_instructions_clinique_cleanser():
    print(file[5])


def read_instructions_new_product():
    print(file[6])


def read_instructions_new_product1():
    print(file[7])


def read_instructions_new_product2():
    print(file[8])


def read_instructions_new_product3():
    print(file[9])


def read_instructions_new_product4():
    print(file[10])


def read_instructions_new_product5():
    print(file[11])


def read_instructions_new_product6():
    print(file[12])
