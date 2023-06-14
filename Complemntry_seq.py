
def Complemtry_Seq(Sequence):
	
		# complement strand
		Sequence = Sequence.replace("A", "t").replace(
			"C", "g").replace("T", "a").replace("G", "c")
		Sequence = Sequence.upper()
		return Sequence
		

seq = "CTCGGATTTGTAAAGATCATGATCTCATACATAGTACCTAGCCATTG"

print(Complemtry_Seq(seq))