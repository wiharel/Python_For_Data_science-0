ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#1
ft_list[1] = "World!"

#2
y = list(ft_list)
y[1] = "France!"
ft_tuple = tuple(y)

#3
ft_set.discard("tutu!")
ft_set.add("Paris!")
sorted_list = sorted(ft_set)

#4
ft_dict["Hello"] = "42Paris!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)