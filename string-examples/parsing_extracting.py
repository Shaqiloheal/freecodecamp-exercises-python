data = 'From james.smith@abdn.ac.uk Sun Jan  9 22:42:53 2022'

atpos = data.find('@')
print(atpos)
# 16

sppos = data.find(' ',atpos)
print(sppos)
# 27

host = data[atpos + 1 : sppos]
print(host)
# abdn.ac.uk