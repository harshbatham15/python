class Train:
	rate=20 #rate is per km 
	trains_avl=[120,121,122,123,124,125,126,127,128,129,130]
	tkts_avl={120:100,121:100,122:100,123:100,124:100,125:100,126:100,127:100,128:100,129:100,130:100}
	stations_dict={
	        120:{"kanpur Central":0,"Panki Dham":5,"Patra":10,"Rura":15,"Jhinjhak":20,"Auraia":25},
	        121:{"kanpur Central":0,"unnao":10,"lucknow":20,"agra":30},
	        122:{"kanpur Central":0,"Aligarh":20,"Delhi":40,"panipat":60},
	        123:{"Kanpur Central":0,"katra":30,"sri nagar":60,"gulmarg":90},
	        124:{"kanpur Central":0,"pandit deen dayal":3,"dehri on soon":6,"kolkata":9},
	        125:{"Kanpur Central":0,"patna":40,"assam":80,"darjeeling":120},
	        126:{"kanpur Central":0,"udaipur":50,"jamnagar":100},
	        127:{"kanpur Central":0,"surat":60,"somnath":120},
	        128:{"kanpur Central":0,"nagpur":70,"bombay":140,"pune":210},
	        129:{"kanpur Central":0,"guwhati":80,"gangtok":160},
	        130:{"kanpur Central":0,"vishakha patnam":90,"andman and nicobar":180}
	        }

	def __init__ (self,name,gender,age,train_num,board,destination,tickets):
		self.name=name
		self.gender=gender
		self.age=age
		self.train_num=train_num
		self.board=board
		self.destination=destination
		self.tickets=tickets

	def book_tickets(self):
		if self.train_num in self.trains_avl:
			if (self.board and self.destination in self.stations_dict[self.train_num]) and (self.stations_dict[self.train_num][self.destination]>self.stations_dict[self.train_num][self.board]):
				if self.tickets<=self.tkts_avl[self.train_num]:
					cost=amount=(self.tickets*self.rate*((self.stations_dict[self.train_num][self.destination])-(self.stations_dict[self.train_num][self.board])))
					print(f'''\nCongrats! Your Tickets are Booked.\nName:{self.name}  Sex:{self.gender}  Age:{self.age}\nTrain Number:{self.train_num}  From:{self.board}  To:{self.destination}\nCost={cost}''')
					print("Seat Number: ")
					i=self.tickets
					k=0
					while(i!=0):
						if i!=1:
							print(self.tkts_avl[self.train_num]-k,end=",")
						else:
							print(self.tkts_avl[self.train_num]-k)
						i-=1
						k+=1
					self.tkts_avl[self.train_num]-=self.tickets
				else:
					print("Tickets not available")
			else:
				print("Train does not run on selected routes")
		else:
			print("train not available")


name=input("Enter Name: ")
gender=input("Enter Sex: ")
age=int(input("Enter Age: "))
train_num=int(input("Enter Train Number: "))
board=input("Enter Boarding City: ")
destination=input("Enter Destination City: ")
tickets=int(input("Enter Number of Tickets: "))

passenger=Train(name,gender,age,train_num,board,destination,tickets)
passenger.book_tickets()
passenger.book_tickets()