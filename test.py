'''
Created on 2018年5月24日

@author: rasca1
'''
import time,model
from lib import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
models=model.model()
chrome_options = Options()
#headless模式运行
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
#不加载图片
#chrome_options.add_argument('blink-settings=imagesEnabled=false')
chrome_options.add_argument("window-size=1400,600");
#调用当前chrome用户数据 cookie登陆方式
#chrome_options.add_argument(r'user-data-dir=%s'%models.read_config('chrome_user_data'))
#chrome_options.add_argument(r'user-data-dir=C:\Users\63571\AppData\Local\Google\Chrome\User Data')
chrome_options.add_argument('--hide-scrollbars') 
chrome_options.binary_location = r'%s'%models.read_config('chrome_path')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('http://www.baidu.com')
driver.add_cookie({'domain':'.qq.com','name':'key-aaxxaaaaa', 'value':'value-bbbb','path':'/'})
driver.set_page_load_timeout(8) 
driver.get('http://www.qq.com')
#print(driver.page_source)
#time.sleep(8)
#driver.quit()
'''
list_url=['http://iy.qq.com', 'http://kd.qq.com', 'http://dt.qq.com', 'http://dw.qq.com', 'http://dv.qq.com', 'http://du.qq.com', 'http://dh.qq.com', 'http://df.qq.com', 'http://ef.qq.com', 'http://ke.qq.com', 'http://lb.qq.com', 'http://le.qq.com', 'http://ld.qq.com', 'http://kp.qq.com', 'http://pc.qq.com', 'http://pb.qq.com', 'http://kt.qq.com', 'http://l2.qq.com', 'http://l1.qq.com', 'http://l3.qq.com', 'http://l5.qq.com', 'http://lh.qq.com', 'http://lk.qq.com', 'http://ll.qq.com', 'http://ln.qq.com', 'http://lj.qq.com', 'http://kf.qq.com', 'http://kg.qq.com', 'http://kl.qq.com', 'http://pp.qq.com', 'http://py.qq.com', 'http://pd.qq.com', 'http://pg.qq.com', 'http://qc.qq.com', 'http://qd.qq.com', 'http://jz.qq.com', 'http://qe.qq.com', 'http://os.qq.com', 'http://qh.qq.com', 'http://qi.qq.com', 'http://ql.qq.com', 'http://qm.qq.com', 'http://qk.qq.com', 'http://pl.qq.com', 'http://ps.qq.com', 'http://pr.qq.com', 'http://pk.qq.com', 'http://qq.qq.com', 'http://qt.qq.com', 'http://qr.qq.com', 'http://qb.qq.com', 'http://rl.qq.com', 'http://rk.qq.com', 'http://ru.qq.com', 'http://sd.qq.com', 'http://sc.qq.com', 'http://sh.qq.com', 'http://sf.qq.com', 'http://sb.qq.com', 'http://se.qq.com', 'http://sg.qq.com', 'http://sj.qq.com', 'http://sk.qq.com', 'http://sl.qq.com', 'http://sm.qq.com', 'http://vp.qq.com', 'http://vs.qq.com', 'http://vo.qq.com', 'http://vm.qq.com', 'http://rc.qq.com', 'http://qf.qq.com', 'http://rm.qq.com', 'http://rp.qq.com', 'http://qp.qq.com', 'http://qs.qq.com', 'http://ry.qq.com', 'http://ro.qq.com', 'http://wp.qq.com', 'http://wt.qq.com', 'http://wx.qq.com', 'http://wj.qq.com', 'http://x5.qq.com', 'http://rx.qq.com', 'http://wa.qq.com', 'http://wb.qq.com', 'http://xh.qq.com', 'http://rb.qq.com', 'http://wk.qq.com', 'http://wm.qq.com', 'http://wo.qq.com', 'http://wl.qq.com', 'http://wy.qq.com', 'http://x1.qq.com', 'http://wz.qq.com', 'http://wg.qq.com', 'http://wf.qq.com', 'http://vi.qq.com', 'http://vr.qq.com', 'http://vy.qq.com', 'http://w5.qq.com', 'http://s3.qq.com', 'http://rz.qq.com', 'http://sy.qq.com', 'http://tj.qq.com', 'http://yu.qq.com', 'http://zb.qq.com', 'http://zc.qq.com', 'http://xd.qq.com', 'http://zf.qq.com', 'http://zg.qq.com', 'http://zj.qq.com', 'http://zl.qq.com', 'http://yr.qq.com', 'http://xq.qq.com', 'http://zt.qq.com', 'http://zq.qq.com', 'http://zw.qq.com', 'http://ws.qq.com', 'http://wq.qq.com', 'http://xt.qq.com', 'http://xs.qq.com', 'http://xj.qq.com', 'http://ye.qq.com', 'http://yi.qq.com', 'http://yl.qq.com', 'http://ym.qq.com', 'http://yx.qq.com', 'http://yw.qq.com', 'http://wr.qq.com', 'http://xw.qq.com', 'http://yz.qq.com', 'http://yy.qq.com', 'http://xb.qq.com', 'http://xg.qq.com', 'http://xc.qq.com', 'http://x6.qq.com', 'http://xx.qq.com', 'http://z5.qq.com', 'http://xk.qq.com', 'http://yd.qq.com', 'http://xm.qq.com', 'http://xl.qq.com', 'http://yh.qq.com', 'http://yn.qq.com', 'http://yo.qq.com', 'http://y1.qq.com', 'http://zz.qq.com', 'http://zy.qq.com', 'http://yj.qq.com', 'http://yp.qq.com', 'http://ys.qq.com', 'http://yt.qq.com', 'http://zd.qq.com', 'http://xy.qq.com', 'http://zm.qq.com', 'http://zx.qq.com','http://l.qq.com', 'http://t.qq.com', 'http://p.qq.com', 'http://b.qq.com', 'http://d.qq.com', 'http://i.qq.com', 'http://o.qq.com', 'http://x.qq.com', 'http://0.qq.com', 'http://4.qq.com', 'http://u.qq.com', 'http://5.qq.com', 'http://q.qq.com', 'http://v.qq.com', 'http://9.qq.com', 'http://c.qq.com', 'http://e.qq.com', 'http://g.qq.com', 'http://s.qq.com', 'http://6.qq.com', 'http://8.qq.com', 'http://a.qq.com', 'http://1.qq.com', 'http://7.qq.com', 'http://h.qq.com', 'http://z.qq.com', 'http://m.qq.com']
list_urls=[]
for i in list_url:
    list_urls.append(i)
    if len(list_urls)==5:
        print(list_urls)
        list_urls=[]
print(list_urls)
'''