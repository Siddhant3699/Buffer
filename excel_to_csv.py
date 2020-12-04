import pandas as pd
from os import linesep

if __name__ == '__main__':
	filename = input('Enter complete path of file : ')
	data = pd.DataFrame(pd.read_excel(filename))
	
	#Output file will be saved as output.csv in current working directory
	data.to_csv('output.csv',
				header=True,
				index=False,
				line_terminator=linesep,
				encoding='utf-8')

	print('File converted...\nCheck "output.csv" in current working directory...')