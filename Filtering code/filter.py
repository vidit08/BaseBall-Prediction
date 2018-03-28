import glob

params = ['id','visteam', 'hometeam', 'date', 'starttime', 'daynight', 'temp', 'winddir', 'windspeed', 'fieldcond', 'precip', 'sky', 'attendance']
result = []
temp = []	
teams = ['ANA', 'ARI', 'ATL', 'BAL', 'BOS', 'CHA', 'CHN', 'CIN', 'CLE', 'COL', 'DET', 'FLO', 'HOU', 'KCA', 'LAN', 'MIL', 'MIA', 'MIN', 'NYA', 'NYN', 'OAK', 'PHI', 'PIT', 'SDN', 'SEA', 'SFN', 'SLN', 'TBA', 'TEX', 'TOR', 'WAS']

x = open( 'all.txt', 'w')
for z in teams:
	folder = '/home/vidit/Downloads/2010-16/*'+z+'.*'
	team = glob.glob(folder)
	team.sort()
	# print len(team)
	

	for name in team:
		# print name
		try:
			with open(name) as f:
				print name
				d = f.readlines()
				
				for line in d: 
					line = line.split(',')

					if line[0] == 'id':
						result.append(temp)
						if temp != []:
							x.write(','.join(temp))
							x.write('\n')
						temp = []
						temp.append(line[1][:-2])

					if line[0] == 'info' and line[1] in params:
						temp.append(line[2][:-2])
		except:
			print 'error'