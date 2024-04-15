# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# * url = "http://www.github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

# https://www.codewars.com/kata/514a024011ea4fb54200004b


def find_site_name(url:str) -> str:
    substr1:str = "www."
    substr2:str = ".com"

    index1:int = url.index(substr1) + len(substr1) 
    index2:int = url.index(substr2)

    output:str = ""

    for i in range(index1, index2):
        output = output + url[i]
    return output

def find_site_names(url:str) -> str:
    writing:bool = 0
    output:str = ''

    for char in url:
        if writing:
            output = output + char 
        if char == '.':
            writing = not writing
    return output.replace('.', '')

print(find_site_name("http://www.google.com"))
print(find_site_name("http://www.yahoo.com"))
print(find_site_name("http://www.ask.com"))

print(find_site_names("http://maps.google.com"))
print(find_site_names("http://www.yahoo.com"))
print(find_site_names("http://www.ask.net"))
print(find_site_names("http://subdomain.site.restaurant"))
print(find_site_names("http://subdomain.site.co.uk"))