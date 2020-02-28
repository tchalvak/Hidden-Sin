#INPUT: 0001110001110 0
#sys.argv[1]: parameter settings in binary form, thirteen digits long: "0001110001110" 
#sys.argv[2]: do you want to see the UR treelets?


#OUTPUT:  tab delimited text file with the parameter settings as the filename
# listing all the SR produced by the language, and the UR for each, if sys.argv[2] is on
# 
# 


import sys
from collections import defaultdict

para = sys.argv[1]
if len(para) != 13:
    print "\nWrong parameter settings length, it should be thirteen digits long! Try again!"
    exit()
try:
    if int(sys.argv[2]) == 1:
        URon = True
    else:
        URon = False
except:
    print "did you enter a second argument?  Do you want to see the URs or not?"
    exit()
try:
    if int(sys.argv[3]) == 1:
        gaps = True
    else:
        gaps = False
except:
    print "Missing Argument 3: Do you want to see gaps for the missing/unrealizable URs?"
    exit()

all = open("COLAG_2011_flat.txt")
out_filename = "output/"+para+".txt"

SR_dict = defaultdict(lambda:'')
SR_dict["header"] = ["UR #", "ILLOC", "SR"]
highest_line5 = 0
count = 0
for line in all.readlines():
    line = line.split("\t")
    if line[0] == para:
        count += 1
        #print "found matching parameter and UR #:"+line[5]
        if line[5] > highest_line5:
            highest_line5 = int(line[5])
        if URon == True:
            #print "true"
            SR_dict[int(line[5])] = [line[1], line[2], line[3]]
            #print SR_dict[int(line[5])]
        if URon == False:
            #print "false"
            SR_dict[int(line[5])] = [line[1], line[2]]
            #print SR_dict[int(line[5])]
print "\nFound "+str(count)+" SRs for this parameter"
with open(out_filename, 'w') as f:
    outp = ''
    for x in SR_dict["header"]:
        outp += x+"\t"
    f.write(outp+"\n")
    if gaps == True:
        for x in range(0,highest_line5+1):
            #print SR_dict[x]
            outp = str(x)+":\t"
            for col in SR_dict[x]:
                outp += col+"\t"
            #print outp
            f.write(outp+"\n")
    if gaps == False:
        for x in range(0,highest_line5+1):
            if len(SR_dict[x]) > 1:
                outp = str(x)+":\t"
                for col in SR_dict[x]:
                    outp += col+"\t"
                #print outp
                f.write(outp+"\n")
print "Printed to:    "+"output/"+para+".txt\n"




        # SR = line[5]+"\t"
        # for x in range(1, length):
        #     SR += line[x]+"\t"
        # f.write(SR+"\n")
    #if count == 1230:
        #print "all SRs for this parameter have been found"
        #break

