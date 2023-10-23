#USB Shopper.

usb_stick_price = 6
budget = 50
num_usb_sticks = budget // usb_stick_price
remaining_budget = budget % usb_stick_price
print(f"The girl can buy {num_usb_sticks} USB sticks.")
print(f"She will have £{remaining_budget} left.")
