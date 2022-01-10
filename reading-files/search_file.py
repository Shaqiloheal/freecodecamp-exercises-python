fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip() # strips newline
    if line.startswith('From:'):
        print(line)

# From: james.smith@abdn.ac.uk
# From: carol.anderson@gmail.com
# From: solid.snake@mgs.co.jp
# From: hal.emmerich@zoe.co.uk
# ....
