from flask import Flask, render_template
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from bs4 import BeautifulSoup 
import requests

#don't change this
matplotlib.use('Agg')
app = Flask(__name__) #do not change this

#insert the scrapping here
url_get = requests.get('https://top-1000-sekolah.ltmpt.ac.id/')
soup = BeautifulSoup(url_get.content,"html.parser")

#find your right key here
table = soup.find('div', attrs={'class':'grid-view'})
table.find_all('td', attrs={'style':'text-align:center'})[:5]

#Finding row length
row = table.find_all('td', attrs={'style':'text-align:left'})
row_length = len(row)
row_length

tableHead = soup.thead
tableHead

#Do the scrapping process here (please change this markdown with your explanation)

tableHead = soup.thead
tableHead

row_headers = []
for x in tableHead.find_all('tr'):
    for y in x.find_all('th'):
        row_headers.append(y.text)
row_headers

tableBody = soup.tbody
tableBody

tableValues = []
for x in tableBody.find_all('tr')[0:]:
    td_tags = x.find_all('td')
    td_val = [y.text for y in td_tags]
    tableValues.append(td_val)
tableValues


temp = df[::-1]
temp


#change into dataframe
df = pd.DataFrame(temp)

#insert data wrangling here
df.dtypes
df['Ranking'] = df['Ranking'].astype('int64')
df=df.set_index('Nilai Total')

#end of data wranggling 

@app.route("/")
def index(): 
	
	card_data = f'{data["df"].mean().round(2)}' #be careful with the " and ' 

	# generate plot
	ax = df.plot(figsize = (20,9)) 
	
	# Rendering plot
	# Do not change this
	figfile = BytesIO()
	plt.savefig(figfile, format='png', transparent=True)
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue())
	plot_result = str(figdata_png)[2:-1]

	# render to html
	return render_template('index.html',
		card_data = card_data, 
		plot_result=plot_result
		)


if __name__ == "__main__": 
    app.run(debug=True)