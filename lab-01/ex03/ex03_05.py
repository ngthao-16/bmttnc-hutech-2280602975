def demsolanxuathien(lst):
    count_dict={}
    for item in lst:
        if item in count_dict:
            count_dict[item]+=1
        else:
            count_dict[item]=1
    return count_dict
input_string=input("nhap ds cac tu , cach nhau bang dau cach:")
wordlist=input_string.split()
solanxuathien=demsolanxuathien(wordlist)
print("so lan xuat hien:",solanxuathien)