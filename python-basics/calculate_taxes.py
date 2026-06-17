def my_pay(num_hours, hourly_rate, tax_rate):
    gross_pay = num_hours * hourly_rate
    taxes = gross_pay * tax_rate
    net_pay = gross_pay - taxes
    return net_pay
net_pay = my_pay(40, 28, 28/100)
print(f"My net pay is: ${net_pay:.2f}")
