#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: May 2021
# This program properly formats a mailing address and uses a default value


def address_formatting(name, street_number, street_name, city, province,
                       postal_code, apartment_number=None):
    # This function formats the address

    address = name + "\n"
    if apartment_number is not None:
        address = address + apartment_number + "-"
    address = address + street_number + " " + street_name + "\n" \
        + city + " " + province + "  " + postal_code

    return address


def main():
    # This function gets the address information
    apartment_number_input = None

    # Input
    print("This program properly formats your mailing address.")
    print("")
    name_input = input("Enter your full name: ")
    apartment_question_input = input("Do you live in an apartment "
                                      "(yes/no)?: ")
    if apartment_question_input == "yes":
        apartment_number_input = input("Enter your apartment number: ")
    street_number_input = input("Enter your street number: ")
    street_name_input = input("Enter your street name and type: ")
    city_input = input("Enter your city: ")
    province_input = input("Enter the abbreviation of your province: ")
    postal_code_input = input("Enter your postal code: ")

    # Call functions
    if apartment_number_input is not None:
        mailing_address = address_formatting(name_input,
                                             street_number_input,
                                             street_name_input,
                                             city_input,
                                             province_input,
                                             postal_code_input,
                                             apartment_number_input)
    else:
        mailing_address = address_formatting(name_input,
                                             street_number_input,
                                             street_name_input,
                                             city_input,
                                             province_input,
                                             postal_code_input)

    # Output
    print("")
    print("Your mailing address is:")
    print("")
    print(mailing_address.upper())
    print("\nDone.")


if __name__ == "__main__":
    main()
