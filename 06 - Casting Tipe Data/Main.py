#casting : merubah dari satu tipe ke tipe lain
print("=====Integer======")
data_int =0
print("data = ",data_int,", type = ",type(data_int))


data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)

print("data = ",data_float,", type = ",type(data_float))
print("data = ",data_str,", type = ",type(data_str))
print("data = ",data_bool,", type = ",type(data_bool))

print("=====Float======")
data_float =9.5
print("data = ",data_float,", type = ",type(data_float))


data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)

print("data = ",data_int,", type = ",type(data_int))
print("data = ",data_str,", type = ",type(data_str))
print("data = ",data_bool,", type = ",type(data_bool))