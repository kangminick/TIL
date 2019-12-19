#
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/search')
def search():
    return render_template('lookup.html')

@app.route('/nation')
def nation():
    Name = request.args.get('query')
    url = f"https://search.naver.com/search.naver?query=(Name)"
    req = requests.get(url).text
    data = BeautifulSoup(req, 'html.parser')

    # image = data.select('#main_pack > div:nth-child(11) > div > div.contents03_sub > div > div.nacon_area._info_area > div.naflag_box > div.img_naflag > a > img')
    # nation_img = image
    language = data.select('#dss_nation_tab_summary_content > dl.lst_nadata > dd:nth-child(2) > a')
    lan = language
    wid =  data.select('#dss_nation_tab_summary_content > dl.lst_nadata > dd:nth-child(4) > span.over_text.overtext_maxwidth')
    widt = wid
    number = data.select('#dss_nation_tab_summary_content > dl.lst_nadata > dd:nth-child(6) > span.over_text.overtext_maxwidth')
    num = number
    history = data.select('#dss_nation_tab_summary_content > dl.lst_nadata > dd:nth-child(12) > p')
    his = history
    return render_template('nation.html', Name = Name,  lan = lan, widt = widt, num = num, his = his)

if __name__==("__main__"):
    app.run(debug=True)