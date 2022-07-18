import pandas as pd
import glob
import datetime
from datetime import timedelta
import calendar

def start(sigyo, start_cri_t):
    #関数startの引数start_timeを定義
    #一時変数dt_sigyoutime
    #returnを使って始業時刻からの残業代を計算
    """
    Args:
        datetime.time #df_workから引数を取る
    Returns:
        float: 分
    """
    dt_sigyotime = datetime.datetime.combine(datetime.date.today(), sigyo)
    dt_start_cri_t = datetime.datetime.combine(datetime.date.today(), start_cri_t)
    return (dt_start_cri_t - dt_sigyotime).total_seconds()/60

def end(syugyo, end_cri_t):
    #関数endの引数end_timeを定義
    #一時変数dt_syugyotime
    #returnを使って終業時刻からの残業代を計算
    """
    Args:
        datetime.time
    Returns:
        float: 分
    """
    dt_syugyotime = datetime.datetime.combine(datetime.date.today(), syugyo)
    dt_end_cri_t = datetime.datetime.combine(datetime.date.today(), end_cri_t)
    return (dt_syugyotime - dt_end_cri_t).total_seconds()/60

def make_cal(year, month):
    #月曜日が0となるカレンダー
    c = calendar.Calendar(firstweekday=0)
    cal =c.monthdays2calendar(year, month)

    cal_ext=[]
    for i in cal:
        cal_ext.extend(i)
    cal_ext= pd.DataFrame(cal_ext)
    cal_ext
    #1/1は土曜だからそこが一番上の行になるように0列目の0が続いている段を削除している
    get_index=0
    index_list=[]
    for i in range(len(cal_ext)):
        if cal_ext.iloc[i,0]==0:
            index_list.append(get_index)
        get_index+=1
    cal_ext=cal_ext.drop(index=cal_ext.index[index_list]).reset_index(drop=True).astype(str)
    #1列目を曜日に表記変更
    cal_ext.iloc[:,1] = cal_ext.iloc[:,1].str.replace('6', '日').str.replace('0','月').str.replace('1','火').str.replace('2','水').str.replace('3','木').str.replace('4','金').str.replace('5','土')
    cal_ext[2]="平日"
    for i in range(len(cal_ext)-1):
        if cal_ext.iloc[i,1]=="土":
            cal_ext.iloc[i,2]="土曜"
        elif cal_ext.iloc[i,1]=="日":
            cal_ext.iloc[i,2]="休日"
        else:
            pass

    cal_ext.set_axis(['日付', '曜日', '扱い'], 
                        axis='columns', inplace=True)
    return cal_ext
