# Got a challange realted to dictionary. which I have to solve in python.

str = "AMIT MAURYA"

freq = {};
for s in str:
    if s == " ":
        continue;
    if s not in freq:
        freq[s] = 1;
    else:
        freq[s] += 1;

print(freq['A']);
        
