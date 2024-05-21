# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"14C4.11","system":"readv2"},{"code":"J410100","system":"readv2"},{"code":"15207.0","system":"readv2"},{"code":"24550.0","system":"readv2"},{"code":"24858.0","system":"readv2"},{"code":"22516.0","system":"readv2"},{"code":"30433.0","system":"readv2"},{"code":"42822.0","system":"readv2"},{"code":"23950.0","system":"readv2"},{"code":"8347.0","system":"readv2"},{"code":"33456.0","system":"readv2"},{"code":"5133.0","system":"readv2"},{"code":"104259.0","system":"readv2"},{"code":"48732.0","system":"readv2"},{"code":"53743.0","system":"readv2"},{"code":"704.0","system":"readv2"},{"code":"43090.0","system":"readv2"},{"code":"1784.0","system":"readv2"},{"code":"6650.0","system":"readv2"},{"code":"K51","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ulcerative-colitis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["colitis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["colitis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["colitis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
