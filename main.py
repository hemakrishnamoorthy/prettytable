from prettytable import PrettyTable
my_table = PrettyTable()
my_table.align = "l"
my_table.add_column("Emp ID", [101, 102, 103, 104, 105])
my_table.add_column("Emp Name", ["Jack", "Jim", "Daisy","Mark", "John"])
my_table.add_column("Dept ID", [20, 10, 10, 30, 70])
my_table.add_column("Salary", [7500, 6500, 7900, 8600, 9000])
my_table.add_column("City", ["Dallas", "Chicago","New York", "Jacksonville", "San Francisco"])

print(my_table)