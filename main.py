
            
# import csv

# with open("random_data.csv", "r") as f:
#     data = csv.reader(f)
#     next(data) # Skip header

#     with open("collected_data.csv", "w", newline="") as file:
#         write = csv.writer(file)
#         write.writerow(["Name", "Age", "Score"])

#         # 1. FIX: cleaned list ko loop ke BAHAR likhein taake yeh har baar reset na ho
#         cleaned = [] 

#         for line in data:
#             name = line[0].strip().lower()
#             age = line[1].strip()
#             score = line[2].strip()
            
#             # 2. Pehle missing data check karein (Zyada behtar approach)
#             if name == "":
#                 print("===== NAME IS MISSING! =====")
#                 continue
#             if age == "":
#                 print("===== AGE IS MISSING! =====")
#                 continue
#             if score == "":
#                 print("===== SCORE IS MISSING! =====")
#                 continue 

#             # 3. Phir type conversion check karein
#             try:
#                 age = int(age)
#                 score = int(score)
#             except ValueError:
#                 print("===== NOT FOUND / INVALID DATA =====")
#                 continue  

#             # 4. Ab duplicate check karein (Jab data valid ho chuka ho)
#             title = [name, age, score]
#             if title in cleaned:
#                 print("==== DUPLICATE FOUND & SKIPPED =====")
#                 continue
#             else:
#                 cleaned.append(title)

#             # 5. Finally file mein write karein
#             write.writerow([name, age, score])

# print("\nDATA CLEANING COMPLETE! CHECK CLEAN_DATA.CSV.\n")            




# with open("collected_data.csv", "r") as folder:

#     collect = csv.reader(folder)

#     next(collect)

#     with open("cleaned_data.txt", "w") as report:

#         for num, rows in enumerate (collect,start=1):

#             name1 = rows[0]
#             age1 = int(rows[1])
#             score1 = int(rows[2])

#             report.write(f"===== STUDENT {num} =====\n")
#             report.write(f"Name: {name1}\n")
#             report.write(f"Age: {age1}\n")
#             report.write(f"Score: {score1}\n\n")

# print("Student report created successfully!")



