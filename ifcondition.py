indian=["samosa","thali","dosa"]
chinese=["egg roll","chicken role","egg rice"]
itlian=["pasta","maggi","soup"]
dish=input("enter the dish name :")
if dish in indian:
    print("indian")
elif dish in chinese:
    print("chinese")
elif dish in itlian:
    print("itlaian")
else:
    print("i don't know wheather the dish is chinese or indian or itlian")
