import regexes
def scrap_landlinenumber_from_file(filename):
    file=open(filename,"r")
    landlineNumbers=[]

    for line in file:
        landlineNumbers+=regexes.landlineNumberRegex.findall(line)

    return list(set(landlineNumbers))


def scrap_cellphonenumbers_from_file(filename):
    file=open(filename,"r")
    cellphoneNumbers=[]

    for line in file:
        cellphoneNumbers+=regexes.cellphoneNumberRegex.findall(line)

    return list(set(cellphoneNumbers))


def scrap_emails_from_file(filename):
    file=open(filename,"r")
    emails=[]

    for line in file:
        emails+=regexes.emailRegex.findall(line)

    return list(set(emails))


print(scrap_landlinenumber_from_file("datas_to_scrap.txt"))
print(scrap_cellphonenumbers_from_file("datas_to_scrap.txt"))
print(scrap_emails_from_file("datas_to_scrap.txt"))