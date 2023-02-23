fin = open("Country_domain.txt","r")
fout = open("Country_domain.csv","w")
count=-1
while True:
    count += 1
  
    # Get next line from file

    res = count % 3

    match res:
        case 0:
            line_out = ''
            line = fin.readline()
            if not line:
                break
            line = line.strip()
            line_out= f'"{line}";'
        case 1:
            line = fin.readline()
            if not line:
                break
            line = line.strip()
            line_out += f'"{line}"\n'
        case 2:
            line = fin.readline()
            if not line:
                break
            fout.write(line_out)
            print(line_out)
        case _:
            line = fin.readline()
            if not line:
                break
            




  
    # if line is empty
    # end of file is reached

fin.close()  
fout.close()