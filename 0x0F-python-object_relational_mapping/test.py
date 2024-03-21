special_string="spe@#$ci87al*&"
print("String before conversion: ",special_string)
sample_list= ''
for i in special_string:
    if i.isalnum():
        sample_list += i

print("string after conversion:", sample_list)