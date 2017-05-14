#!/usr/bin/python3
#version 3.0 (final)
#author bikki kumar sha
import os
print("------------------------ADVANCED  INTERACTIVE  DICTIONARY----------------------")
print("                                                                             ")
print("              AAA                   IIIIIIIIII      DDDDDDDDDDDDD            ")
print("             A:::A                  I::::::::I      D::::::::::::DDD         ") 
print("            A:::::A                 I::::::::I      D:::::::::::::::DD       ")
print("           A:::::::A                II::::::II      DDD:::::DDDDD:::::D      ")
print("          A:::::::::A                 I::::I          D:::::D    D:::::D     ")
print("         A:::::A:::::A                I::::I          D:::::D     D:::::D    ")
print("        A:::::A A:::::A               I::::I          D:::::D     D:::::D    ")
print("       A:::::A   A:::::A              I::::I          D:::::D     D:::::D    ")
print("      A:::::A     A:::::A             I::::I          D:::::D     D:::::D    ")
print("     A:::::AAAAAAAAA:::::A            I::::I          D:::::D     D:::::D    ")
print("    A:::::::::::::::::::::A           I::::I          D:::::D     D:::::D    ")
print("   A:::::AAAAAAAAAAAAA:::::A          I::::I          D:::::D    D:::::D     ")
print("  A:::::A             A:::::A       II::::::II      DDD:::::DDDDD:::::D      ")
print(" A:::::A               A:::::A      I::::::::I      D:::::::::::::::DD       ")
print("A:::::A                 A:::::A     I::::::::I      D::::::::::::DDD         ")
print("AAAAAAA                  AAAAAAA    IIIIIIIIII      DDDDDDDDDDDDD            ")
print("                                                                             ")
print("                                              bikkikumarsha@gmail.com        ")
print("-------------------------------------------------------------------------------")
              
print("WELCOME!! THIS TOOL IS USED TO GENERATE A CUSTOM DICTIONARY BASED ON USER PERSONAL DATA THAT MIGHT CONTAIN POTENTIAL PASSWORDS.....")
print("Press Enter To Continue_",end="")
input()
print("\n\n")
print("ENTER THE DETAILS OF THE VICTIM: PRESS ENTER TO SKIP... \n")
d1 = input("Enter the first name:  ")
d2 = input("Enter the last name:  ")
d3 = input("Enter the nick-name:  ")
d4 = input("Enter date of birth[DDMMYYYY]:  ")
d5 = input("Enter any significant date/wedding aneversary[DDMMYYYY]:  ")
d6 = input("Enter the company name/organization name/shop name:  ")
d7 = input("Enter the partner's name:  ")
d8 = input("Enter the pet's name:  ")
print("Enter any three additional key-words such as faviorate 'team/player/car/food' ")
k1= input("Enter special keyword number 1:  ")
k2= input("Enter special keyword number 2:  ")
k3= input("Enter special keyword number 3:  ")
print("\n")
pz= int(input("[*] ENTER THE MINIMUM PASSWORD LENGTH: "))

print("\n")
print("[*] WORKING ....\n")
print("[*] GENERATING YOUR WORDLIST, PLEASE WAIT ....\n")
file1= open("storedemo",'a')

def itt(d1,d2,d3,d7):
	ctr=0
	while(ctr<=100):
		sfl(d1,"",str(ctr))
		sfl(d7,"",str(ctr))
		sfl(d1,d2,str(ctr))
		sfl(d1,d7,str(ctr))
		sfl(d2,d3,str(ctr))
		sfl(d3,d7,str(ctr))
		ctr+=1

def matcher(s1,s2,s3,s4,s5,s6,s7,s8,k1,k2,k3):
#matches logial data combination for potential passwords
#breaks down date into dd, ddmm, mmyy, yyyy
	s41=s4[0:2]
	s42=s4[0:4]
	s43=s4[6:8]
	s44=s4[4:8]
	s45=s4[2:4]
	s51=s5[0:2]
	s52=s5[0:4]
	s53=s5[6:8]
	s54=s5[4:8]
	s55=s5[2:4]
	s4m=""
	s5m=""
	s4M=""
	s5M=""
	month=[' ','jan','feb','march','april','may','june','july','august','sept','oct','nov','dec']
	MONTH=[' ','january','february','march','april','may','june','july','august','september','october','november','december']
	if not s45:
		pass
	else:
		for position, ele in enumerate(month):
			if (position == int(s45)):
				s4m=str(ele)
	if not s55:
		pass
	else:
		for position, ele in enumerate(month):
			if (position == int(s55)):
				s5m=str(ele)

	if not s45:
		pass
	else:
		for position, ELE in enumerate(MONTH):
			if (position == int(s45)):
				s4M=str(ELE)
	if not s55:
		pass
	else:
		for position, ELE in enumerate(MONTH):
			if (position == int(s55)):
				s5M=str(ELE)
	

#todo assing months to new vars
	sfl(s1,"","")
	sfl(s2,"","")
	sfl(s3,"","")
	sfl(s4,"","")
	sfl(s5,"","")
	sfl(s6,"","")
	sfl(s7,"","")
	sfl(s8,"","")
	sfl(k1,"","")
	sfl(k2,"","")
	sfl(k3,"","")
	sfl(s1,s2,"")
	sfl(s1,s41,"")
	sfl(s1,s42,"")
	sfl(s1,s43,"")
	sfl(s1,s44,"")
	sfl(s1,s4m,"")
	sfl(s1,s4M,"")
	sfl(s1,s4m,s44)
	sfl(s1,s4M,s44)
	sfl(s1,s41,s4m)
	sfl(s1,s4M,s41)
	sfl(s3,s41,"")
	sfl(s3,s42,"")
	sfl(s3,s43,"")
	sfl(s3,s44,"")
	sfl(s3,s4m,"")
	sfl(s3,s4M,"")
	sfl(s3,s4m,s41)
	sfl(s3,s4M,s41)
	sfl(s3,s4m,s44)
	sfl(s3,s4M,s44)

	sfl(s7,s41,"")
	sfl(s7,s42,"")
	sfl(s7,s43,"")
	sfl(s7,s44,"")
	sfl(s7,s4m,"")
	sfl(s7,s4M,"")
	sfl(s7,s4m,s41)
	sfl(s7,s4M,s41)
	sfl(s7,s4m,s44)
	sfl(s7,s4M,s44)
	sfl(s6,s41,"")
	sfl(s6,s42,"")
	sfl(s6,s43,"")
	sfl(s6,s44,"")
	sfl(s6,s4m,"")
	sfl(s6,s4M,"")
	sfl(s6,s4m,s41)
	sfl(s6,s4M,s41)
	sfl(s1,s51,"")
	sfl(s1,s52,"")
	sfl(s1,s53,"")
	sfl(s1,s54,"")
	sfl(s1,s5m,"")
	sfl(s1,s5M,"")
	sfl(s1,s5m,s51)
	sfl(s1,s5M,s51)
	sfl(s3,s51,"")
	sfl(s3,s52,"")
	sfl(s3,s53,"")
	sfl(s3,s54,"")
	sfl(s3,s5m,"")
	sfl(s3,s5M,"")
	sfl(s3,s5m,s51)
	sfl(s3,s5M,s51)
	sfl(s7,s51,"")
	sfl(s7,s52,"")
	sfl(s7,s53,"")
	sfl(s7,s54,"")
	sfl(s7,s5m,"")
	sfl(s7,s5M,"")
	sfl(s7,s5m,s54)
	sfl(s7,s5M,s54)
	sfl(s7,s5m,s51)
	sfl(s7,s5M,s51)
	sfl(s6,s54,"")
	sfl(s1,k1,"")
	sfl(s1,k2,"")
	sfl(s1,k3,"")
	sfl(s6,k1,"")
	sfl(s6,k2,"")
	sfl(s6,k3,"")
	sfl(s1,s2,"")
	sfl(s1,s3,"")
	sfl(s1,s4,"")
	sfl(s1,s5,"")
	sfl(s3,s4,"")
	sfl(s3,s5,"")
	sfl(s4,s5,"")
	sfl(s1,s6,"")
	sfl(s3,s6,"")
	sfl(s4,s6,"")
	sfl(s1,s7,"")
	sfl(s2,s7,"")
	sfl(s3,s7,"")
	sfl(s4,s7,"")
	sfl(s5,s7,"")
	sfl(s1,s8,"")
	sfl(s1,s2,s41)
	sfl(s1,s2,s42)
	sfl(s1,s2,s43)
	sfl(s1,s2,s44)
	sfl(s1,s2,s4m)
	sfl(s1,s2,s4M)
	sfl(s1,s2,str(s41)+str(s4m))
	sfl(s1,s2,str(s41)+str(s4M))
	sfl(s1,s2,s51)
	sfl(s1,s2,s52)
	sfl(s1,s2,s53)
	sfl(s1,s2,s54)
	sfl(s1,s2,s5m)
	sfl(s1,s2,s5M)
	sfl(s1,s2,str(s51)+str(s5m))
	sfl(s1,s2,str(s51)+str(s5M))
	sfl(s2,s3,s41)
	sfl(s2,s3,s42)
	sfl(s2,s3,s43)	
	sfl(s2,s3,s44)
	sfl(s2,s3,s4m)
	sfl(s2,s3,s4M)
	sfl(s2,s3,str(s41)+str(s4m))
	sfl(s2,s3,str(s41)+str(s4M))

	sfl(s1,s7,s41)
	sfl(s1,s7,s42)
	sfl(s1,s7,s43)
	sfl(s1,s7,s44)
	sfl(s1,s7,s4m)
	sfl(s1,s7,s4M)
	sfl(s1,s7,str(s41)+str(s4m))
	sfl(s1,s7,str(s41)+str(s4M))

	sfl(s3,s7,s41)
	sfl(s3,s7,s42)
	sfl(s3,s7,s43)
	sfl(s3,s7,s44)
	sfl(s3,s7,s4m)
	sfl(s3,s7,s4M)
	sfl(s3,s7,str(s41)+str(s4m))
	sfl(s3,s7,str(s41)+str(s4M))

	sfl(s1,s7,s51)
	sfl(s1,s7,s52)
	sfl(s1,s7,s53)
	sfl(s1,s7,s54)
	sfl(s1,s7,s5m)
	sfl(s1,s7,s5M)
	sfl(s1,s7,str(s51)+str(s5m))
	sfl(s1,s7,str(s51)+str(s5M))

	sfl(s3,s7,s51)
	sfl(s3,s7,s52)
	sfl(s3,s7,s53)
	sfl(s3,s7,s54)
	sfl(s3,s7,s5m)
	sfl(s3,s7,s5M)
	sfl(s3,s7,str(s51)+str(s5m))
	sfl(s3,s7,str(s51)+str(s5M))
	sfl(s2,s44,"")	
	sfl(s2,s54,"")
	sfl(s8,s44,"")	
	sfl(s8,s54,"")
	sfl(k1,s44,"")
	sfl(k2,s44,"")
	sfl(k3,s44,"")
	sfl(k1,s54,"")
	sfl(k2,s54,"")
	sfl(k3,s54,"")
	sfl(s1,s2,s4)
	sfl(s1,s2,s5)
	sfl(s1,s2,s6)
	sfl(s2,s3,s6)
	sfl(s1,s2,s7)
	sfl(s1,s4,s7)
	sfl(s1,s5,s7)
	sfl(s1,s2,k1)
	sfl(s1,s2,k2)
	sfl(s1,s2,k3)
	sfl(s1,s7,k1)
	sfl(s1,s7,k2)
	sfl(s1,s7,k3)
	sfl("","rocks",s1)
	sfl("i","love",s8)
	sfl("is","great",s8)
	sfl(s1,"love",d7)
	sfl("","love",d7)
	sfl("my","love",d7)
	sfl(s1,"loves",d7)
	sfl(s3,"loves",d7)
	sfl(s3,"love",d7)
	sfl(d1,d7,"forever")
	sfl(d1,"and",d7)
	sfl(d1,d7,"alwaysandforever")
	sfl("ilove","you",d7)
	sfl("i","loveyou",d7)	
	sfl("i","loveYou",d7)
	sfl("i", "love", k1)
	sfl("i", "love", k2)
	sfl("i", "love", k3)
	sfl("i", "like", k1)
	sfl("i", "like", k2)
	sfl("i", "like", k3)
	sfl(k1,"","rocks")	
	sfl(k2,"","rocks")	
	sfl(k3,"","rocks")	
	sfl(k1,"is","best")
	sfl(k2,"is","best")
	sfl(k3,"is","best")	
	sfl(k1,"isthe","best")
	sfl(k2,"isthe","best")
	sfl(k3,"isthe","best")	
	sfl(k1,"is","great")
	sfl(k2,"is","great")
	sfl(k3,"is","great")	

def sfl(s1,s2,s3):
#feeds all possible combination to the cap
	cap(s1,s2,s3)
	cap(s1,s3,s2)
	cap(s2,s1,s3)
	cap(s2,s3,s1)
	cap(s3,s1,s2)
	cap(s3,s2,s1)

def cap(s1,s2,s3):
#sends capitalized combination to shuffler
	sym(s1,s2,s3)	
	sym((s1).upper(),s2,s3)
	sym(s1,s2.upper(),s3)
	sym(s1,s2,s3.upper())
	if not s1:
		pass
	else:
		sym((s1[0]).upper()+s1[1:],s2,s3)
	if not s2:
		pass
	else:
		sym(s1,(s2[0]).upper()+s2[1:],s3)
	if not s3:
		pass
	else:
		sym(s1,s2,(s3[0]).upper()+s3[1:])

def sym(s1,s2,s3):
#adds symbols to the passwords
	slist=['@','_','!','$','?',' ','01','02','03','04','05','06','07','08','09','001','002','003','004','005','006','007','008','009',]
	for s in slist:
		sfl3(s1,s2,s3)
		sfl3((s+s1),s2,s3)
		sfl3(s1,(s+s2),s3)
		sfl3(s1,s2,(s+s3))
		sfl3(s1,s2,(s3+s))

def sfl3(s1,s2,s3):
#shuffles the data for all possible logical combination
	file1.write(s1+s2+ "\n")	
	file1.write(s1+s3+ "\n")
	file1.write(s2+s1+ "\n")	
	file1.write(s2+s3+ "\n")
	file1.write(s3+s1+ "\n")	
	file1.write(s3+s2+ "\n")
	file1.write(s1+s2+s3+ "\n")
	file1.write(s1+s3+s2+ "\n")
	file1.write(s2+s1+s3+ "\n")
	file1.write(s2+s3+s1+ "\n")	
	file1.write(s3+s1+s2+ "\n")
	file1.write(s3+s2+s1+ "\n")

matcher(d1,d2,d3,d4,d5,d6,d7,d8,k1,k2,k3)
itt(d1,d2,d3,d7)
print("[*] REMOVING DUPLICATE WORDS AND WORDS WITH LENGTH LESS THAN "+str(pz)+" CHARACTERS ....\n\n")
file1.close()

seen = set()
with open("storedemo", "r") as f_in, open("wordlist-aid", "w") as f_out:
    for line in f_in:
        line = line.rstrip()
        if len(line) > pz and line not in seen:
            f_out.write(line + '\n')
            seen.add(line)
os.remove("storedemo")

print("-------------------------------------------------------------------------------")
print("		DICTIONARY SAVED BY THE FOLLOWING ATTRIBUTES: \n")
print("		FILE NAME       :    "+"wordlist-aid")
print("		WORDS GENERATED :    "+str(len(seen)))
print("		FILE SIZE       :    "+str(os.path.getsize("wordlist-aid"))+"	BYTES")
print("-------------------------------------------------------------------------------")

input("\n\nPress Enter key to exit ....")

