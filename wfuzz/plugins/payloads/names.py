from wfuzz.plugin_api.base import wfuzz_iterator

@wfuzz_iterator
class names:
    name = "names"
    description = "Returns possible usernames by mixing the given words, separated by -, using known typical constructions. ie. jon-smith"
    category = ["default"]
    priority = 99

    def __init__(self, startnames, extra):
	self.startnames = startnames
	from sets import Set
	possibleusernames = []
	name = ""
	llist = self.startnames.split("-")

	for x in llist:
	    if name == "":
		name = name + x
	    else:
		name = name + " " + x

	    if " " in name:
		parts = name.split()
		possibleusernames.append(parts[0])
		possibleusernames.append(parts[0]+"."+parts[1])
		possibleusernames.append(parts[0]+parts[1])
		possibleusernames.append(parts[0]+"."+parts[1][0])
		possibleusernames.append(parts[0][0]+"."+parts[1])
		possibleusernames.append(parts[0]+parts[1][0])
		possibleusernames.append(parts[0][0]+parts[1])
		str1=""
		str2=""
		str3=""
		str4=""
		for i in range(0,len(parts)-1):
			str1=str1+parts[i]+"."
			str2=str2+parts[i]
			str3=str3+parts[i][0]+"."
			str4=str4+parts[i][0]
		str5=str1+parts[-1]
		str6=str2+parts[-1]
		str7=str4+parts[-1]
		str8=str3+parts[-1]
		str9=str2+parts[-1][0]
		str10=str4+parts[-1][0]
		possibleusernames.append(str5)
		possibleusernames.append(str6)
		possibleusernames.append(str7)
		possibleusernames.append(str8)
		possibleusernames.append(str9)
		possibleusernames.append(str10)
		possibleusernames.append(parts[-1])
		possibleusernames.append(parts[0]+"."+parts[-1])
		possibleusernames.append(parts[0]+parts[-1])
		possibleusernames.append(parts[0]+"."+parts[-1][0])
		possibleusernames.append(parts[0][0]+"."+parts[-1])
		possibleusernames.append(parts[0]+parts[-1][0])
		possibleusernames.append(parts[0][0]+parts[-1])
	    else:
		possibleusernames.append(name)

	    self.creatednames=possibleusernames
	    self.__count=len(possibleusernames)
	    
    def count(self):
	return self.__count

    def __iter__(self):
	return self

    def next(self):
	if self.creatednames:
	    payl = self.creatednames.pop()
	    return payl
	else:
	    raise StopIteration
		