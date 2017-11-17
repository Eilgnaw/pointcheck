#!/usr/bin/python
#_*_coding:utf-8_*_
import sys

 
# Point类
class Point:  
    lng = ''  
    lat = ''  
  
    def __init__(self,lng,lat):  
        self.lng = lng  
        self.lat = lat  
  
    def show(self):  
        print self.lng,"\t",self.lat  


#采用射线法判断点是否在多边形集内
def isPointsInPolygons(point,xyset):  
    flag = False  
    p = point
    length = len(xyset)  
    p2 = xyset[length-1]
    for i in range(0,length):  
        p1 = xyset[i]
        #点与多边形顶点重合  
        if (p.lng == p1.lng and p.lat == p1.lat) or (p.lng == p2.lng and p.lat == p2.lat):  
            return True
        #判断线段两端点是否在射线两侧  
        if (p2.lat < p.lat and p1.lat >= p.lat) or (p2.lat >= p.lat and p1.lat < p.lat): 
            #线段上与射线 Y 坐标相同的点的 X 坐标  
            if (p2.lat == p1.lat):  
                x = (p1.lng + p2.lng)/2  
            else:  
                x = p2.lng - (p2.lat - p.lat)*(p2.lng - p1.lng)/(p2.lat - p1.lat)  
            #点在多边形的边上  
            if (x == p.lng):  
                return True
            #射线穿过多边形的边界  
            if (x > p.lng):   
                flag = not flag  
        p2 = p1
    return flag  

def pointcheck():
    #加载多边形点到xyset 
    line = '121.42277777778,31.027666666667,121.42797222222,31.016361111111,121.45088888889,31.023666666667,121.44575,31.035027777778'
    line = line.strip(',') 
    strList = line.split(',')  
    pointslen = len(strList)
    xyset = []    
    for i in range(0,pointslen,2):  
        temp = Point(float(strList[i]),float(strList[i+1]))  
        xyset.append(temp) 
        temp.show()

    # lxy = '121.42797222222,31.023666666667'.split(',')#里面的点
    lxy = '121.42797222222,37.023666666667'.split(',') #外面的点
    lx = float(lxy[0])  
    ly = float(lxy[1])
    point = Point(lx,ly)  
    
    if isPointsInPolygons(point,xyset):
        return "在里面"
    return "在外面"    

#调用函数
if __name__=="__main__":
    print (pointcheck())