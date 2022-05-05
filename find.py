print("""
FIND BUG BOUNTY SITES!\n
""")

# Check for errors!
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
# Search for bug bounty sites!
def security_org():
    query = "inurl:/.well-known/security filetype:txt"
 
    for s in search(query, tld="co.in", num=3000, stop=5000, pause=10):
        print(s)

security_org()



