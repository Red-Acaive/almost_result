
import requests
from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True
#from src.database.conn import *
@app.route('/log.html',methods=['GET']) 
def login():
    return render_template("log.html")

@app.route('/membership.html',methods=['GET'])
def membership():
    return render_template("membership.html")

@app.route('/')
def parking_lot():
    #u#rl = 'http://api.data.go.kr/openapi/tn_pubr_prkplce_info_api'


    #params ={'serviceKey' : 'POX/Qqea1zYsMpX+Jc69gnaFc5JQHTWhXuKwuV4MTUtTA96e7pqGxqaZBbVmeRCJYqmcu+kK46p0ZwJNifPaqw==', 'pageNo' : '1', 'numOfRows' : '100', 'type' : 'xml', 'prkplceNo' : '', 'prkplceNm' : '', 'prkplceSe' : '', 'prkplceType' : '', 'rdnmadr' : '', 'lnmadr' : '', 'prkcmprt' : '', 'feedingSe' : '', 'enforceSe' : '', 'operDay' : '', 'weekdayOperOpenHhmm' : '', 'weekdayOperColseHhmm' : '', 'satOperOperOpenHhmm' : '', 'satOperCloseHhmm' : '', 'holidayOperOpenHhmm' : '', 'holidayCloseOpenHhmm' : '', 'parkingchrgeInfo' : '', 'basicTime' : '', 'basicCharge' : '', 'addUnitTime' : '', 'addUnitCharge' : '', 'dayCmmtktAdjTime' : '', 'dayCmmtkt' : '', 'monthCmmtkt' : '', 'metpay' : '', 'spcmnt' : '', 'institutionNm' : '', 'phoneNumber' : '', 'latitude' : '', 'longitude' : '', 'referenceDate' : '', 'instt_code' : '' }


    #response = requests.get(url=url, params=params)
    #if response.status_code == 200:
    #    print(response.text)
    return render_template("index.html")

# @app.route('/')
# def T_map():
#     version = 1
  
#     url = f'https://apis.openapi.sk.com/tmap/geo/reversegeocoding?version={version}&lat={lat}&lon={lon}&coordType={coordType}&addressType={addressType}&callback={callback}&appKey={appKey}'

#     response = requests.get(url=url, params=params)
#     if response.status_code == 200:
#         print(response.text)
#     return render_template("index.html")









# 비동기는 오는 순서대로 처리함
# 동기는 빠른거부터 처리함 => 데이터 두개가 같은 메모리를 공유하는 경우
# => 빠른거부터 처리 => 문제가 있으면 추적이안됨

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)