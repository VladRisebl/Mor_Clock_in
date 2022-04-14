import time,re,requests,random
'''
from Ver
'''
class Fis(object):
      Detail_li = tuple(set([44,45,96,111,102,71,105,107,90,115,112,117,110,101,56,88,76,92,57,58,98,63,77,82,108,103,113,116,1,6,2,11,3,22,4,21,70,16,43,81,23,29]))
      
      def __init__(self,token):
            self.token = token,
            
      def Login_HI(self,li_,device_code = None):
            print(f'当前需要签到{len(li_)}个板块')
            url2='http://floor.huluxia.com/user/signin/ANDROID/4.0'
            
            headers={
            'Connectio':'close',
            'Host':'floor.huluxia.com',
            'Accept-Encoding':'gzip',
            'User-Agent':'okhttp/3.8.1',
            }
            
            if device_code is None:
                  device_code = 'i'
                  
            for k,v in enumerate(li_):
                  dic={
                  'platform':2,
                  'gkey':000000,
                  'app_version':'4.0.0.6.2',
                  'versioncode':20141433,
                  'market_id':'floor_web',
                  '_key':self.token,
                  'device_code':device_code,
                  'cat_id':v,
                  }
                  Sing = requests.get(url=url2,params=dic,headers=headers)
                  if Sing.status_code != 200:
                        print(f'ip暂时拉黑10分钟,当前状态:{Sing.status_code}',end ='\r')
                        exit()               
                  else:
                        Cont = Sing.json()
                        Expr='''第%d个板块,签到经验:%d,连续签到第%d天,下次签到获取经验:%d,'''%(k+1,Cont['experienceVal'],Cont['continueDays'],Cont['nextExperience'])
                        print(Expr,end = '\r')
                  if k + 1 == len(li_):
                        print('\t')
                        toal_exp = len(li_) * Cont['experienceVal']
                        print(f'签到经验:{toal_exp}')
                        print(f'任务完成签到了{k + 1}个板块')
                        
      
      def Acc_status(self,ID_,device_code = None):
            url1 = 'http://floor.huluxia.com/user/info/ANDROID/2.1'
            if device_code is None:
                  device_code = 'i'
            pa = {
            'platfor':2,
            'gkey':000000,
            'app_version':'4.0.0.6.2',
            'versioncode':20141433,
            'market_id':'floor_web',
            'market_id':'floor_web',
            '_key':self.token,
            'device_code':device_code,
            'user_id':ID_,
            }
            
            hed = {
            'Connectio':'close',
            'Host':'floor.huluxia.com',
            'Accept-Encoding':'gzip',
            'User-Agent':'okhttp/3.8.1',
            }
            
            Acc_stus = requests.get(url = url1,params = pa,headers = hed)
            A_s = Acc_stus.json()
            Acc_ = '''
            名字:%s,
            年龄:%d,
            等级:%d,
            当前经验:%d,
            下级经验:%d,
            相差经验:%d
            关注数量:%d,
            发帖数量:%d,
            收藏数量:%d,
            '''%(A_s['nick'],A_s['age'],A_s['level'],A_s['exp'],A_s['nextExp'],A_s['nextExp'] - A_s['exp'],A_s['followingCount'],A_s['postCount'],A_s['favoriteCount'])
            print(Acc_,end = '\r')
                              