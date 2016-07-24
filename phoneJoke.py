# -*- coding:utf-8 -*-
import urllib2, json, sys, smtplib
from email.mime.text import MIMEText

reload(sys)
sys.setdefaultencoding('utf-8')

mail_host = "smtp.163.com"
mail_user = "??????@163.com"
mail_pass = "??????"
mailto_list = ['??????@139.com']

def send_mail(to_list, part1, sub, content):
    me = part1+"<"+mail_user+">"
    msg = MIMEText(content, _subtype='plain', _charset='utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user, mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False

if __name__ == '__main__':
    appkey = "d1604fb9cd8435c9b8d3d915e2680cd9"
    url = 'http://apis.baidu.com/heweather/weather/free?city=xian'
    req = urllib2.Request(url)
    req.add_header("apikey", appkey)
    resp = urllib2.urlopen(req)
    content = resp.read()
    if(content):
        result = json.loads(content)
        result = result['HeWeather data service 3.0'][0]
        cityname = result['basic']['city']
        datetime = result['basic']['update']['loc']
        daily_forecast = result['now']
        weather = daily_forecast['cond']['txt']
        tmp = daily_forecast['tmp']
        aqi = result['aqi']['city']['aqi']
        suggestion = result['suggestion']
        comf = suggestion['comf']['brf']
        sport = suggestion['sport']['brf']
        
        part1 = mail_user
        part2 = cityname + weather + ' ' + u'温度:' + tmp + u'空气质量:' + aqi
        part3 = u'天气:' + comf + '\n' + u'运动:' + sport
        if send_mail(mailto_list, part1, part2, part3):
            print "send msg succeed"
        else:
            print "send msg failed"
    else:
        print "get weather error"

