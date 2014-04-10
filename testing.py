metro = input("Enter Metro: ")
product = input("Enter Product Type: ")
sba = input("SBA Express? ")
unsec = input("Unsecured? ")
loan_amt = float(input("Enter Loan Amount: "))
dep_amt = float(input("Enter Totoal DDA Amount: "))
cash_sec = input("Cash Secure? ")
prepay = input("Standard Prepay? ")
autopay = input("Autopay? ")
oovsi = input("Owner or Investor? ")

def pcl(product):
	if product.lower() == "crem":
		return(.1)
	if product.lower() == "term":
		return(.2)
	if product.lower() == "pf":
		return(.3)
	if product.lower() == "loc":
		return(.4)
	if product.lower() == "sbh":
		return(.5)
def tm(product):
	if product.lower() == "crem":
		return(.1)
	if product.lower() == "term":
		return(.2)
	if product.lower() == "pf":
		return(.3)
	if product.lower() == "loc":
		return(.4)
	if product.lower() == "sbh":
		return(.5)
def metro_o(product):
	if product.lower() == "crem" and metro.lower() == "florida":
		return(.1)
	if product.lower() == "crem" and metro.lower() == "carolinas":
		return(.1)
	if product.lower() == "crem" and metro.lower() == "mid-south":
		return(.1)	
	else:
		return(0)
def prod_discount(product):
	if product.lower() == "crem":
		return(.1)
	if product.lower() == "term":
		return(.2)
	if product.lower() == "pf":
		return(.3)
	if product.lower() == "loc":
		return(.4)
	if product.lower() == "sbh":
		return(.5)
def loan_amt_o(product):
	if loan_amt > 0:
		if product.lower() == "crem":
			if loan_amt<25000:
				return (11)
			if loan_amt>=25000 and loan_amt<100000:
				return (21)
			if loan_amt>=100000 and loan_amt<250000:
				return (31)
			if loan_amt>=250000 and loan_amt<500000:
				return (41)
			if loan_amt>500000:
				return (51)
		if product.lower() == "term":
			if loan_amt<25000:
				return (12)
			if loan_amt>=25000 and loan_amt<100000:
				return (22)
			if loan_amt>=100000 and loan_amt<250000:
				return (32)
			if loan_amt>=250000 and loan_amt<500000:
				return (42)
			if loan_amt>500000:
				return (52)
		if product.lower() == "pf":
			if loan_amt<25000:
				return (13)
			if loan_amt>=25000 and loan_amt<100000:
				return (23)
			if loan_amt>=100000 and loan_amt<250000:
				return (33)
			if loan_amt>=250000 and loan_amt<500000:
				return (43)
			if loan_amt>500000:
				return (53)
		if product.lower() == "loc":
			if loan_amt<25000:
				return (14)
			if loan_amt>=25000 and loan_amt<100000:
				return (24)
			if loan_amt>=100000 and loan_amt<250000:
				return (34)
			if loan_amt>=250000 and loan_amt<500000:
				return (44)
			if loan_amt>500000:
				return (54)
		if product.lower() == "sbh":
			if loan_amt<25000:
				return (15)
			if loan_amt>=25000 and loan_amt<100000:
				return (25)
			if loan_amt>=100000 and loan_amt<250000:
				return (35)
			if loan_amt>=250000 and loan_amt<500000:
				return (45)
			if loan_amt>500000:
				return (55)
def dep_amt_o(product):
	if loan_amt > 0:
		if product.lower() == "crem":
			if loan_amt<10000:
				return (11)
			if loan_amt>=10000 and loan_amt<40000:
				return (21)
			if loan_amt>40000:
				return (51)
		if product.lower() == "term":
			if loan_amt<10000:
				return (11)
			if loan_amt>=10000 and loan_amt<40000:
				return (21)
			if loan_amt>40000:
				return (51)
		if product.lower() == "pf":
			if loan_amt<10000:
				return (11)
			if loan_amt>=10000 and loan_amt<40000:
				return (21)
			if loan_amt>40000:
				return (51)
		if product.lower() == "loc":
			if loan_amt<10000:
				return (11)
			if loan_amt>=10000 and loan_amt<40000:
				return (21)
			if loan_amt>40000:
				return (51)
		if product.lower() == "sbh":
			if loan_amt<10000:
				return (11)
			if loan_amt>=10000 and loan_amt<40000:
				return (21)
			if loan_amt>40000:
				return (51)
def cash_sec_o(product):
	if cash_sec.lower() == "yes":
		if product.lower() == "crem":
			return(.1)
		if product.lower() == "term":
			return(.2)
		if product.lower() == "pf":
			return(.3)
		if product.lower() == "loc":
			return(.4)
		if product.lower() == "sbh":
			return(.5)
	else:
		return (0)
def prepay_o(product):
	if prepay.lower() == "no":
		if product.lower() == "crem":
			return(.1)
		if product.lower() == "term":
			return(.2)
		if product.lower() == "pf":
			return(.3)
		if product.lower() == "loc":
			return(.4)
		if product.lower() == "sbh":
			return(.5)
	else:
		return (0)
def autopay_o(product):
	if autopay.lower() == "no":
		if product.lower() == "crem":
			return(.1)
		if product.lower() == "term":
			return(.2)
		if product.lower() == "pf":
			return(.3)
		if product.lower() == "loc":
			return(.4)
		if product.lower() == "sbh":
			return(.5)
	else:
		return (0)
def oovsi_o(product):
	if oovsi.lower() == "Investor":
		if product.lower() == "crem":
			return(.1)
		if product.lower() == "term":
			return(.2)
		if product.lower() == "pf":
			return(.3)
		if product.lower() == "loc":
			return(.4)
		if product.lower() == "sbh":
			return(.5)
	else:
		return (0)
print ("Your rate is: ", pcl(product)+tm(product)+metro_o(product)+prod_discount(product)+loan_amt_o(product)+dep_amt_o(product)+cash_sec_o(product)+prepay_o(product)+autopay_o(product)+oovsi_o(product))