import csv, matplotlib
from pathlib import Path
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
import matplotlib.font_manager as fm

plt.rcParams.update({'pdf.use14corefonts':True,'ps.useafm':True,'svg.fonttype':'none'})
FONT='Helvetica'
plt.rcParams['font.family']='sans-serif'
plt.rcParams['font.sans-serif']=['Helvetica','Arial','sans-serif']

OBS='#0072B2'; VER='#E69F00'; UNR='#ECEFF1'; BORD='#3A3A3A'; INK='#000000'
FS=8.0; LW=1.05

DATA_PATH=Path(__file__).resolve().parent.parent/'data'/'04_protection_chain_matrix.csv'
rows=list(csv.DictReader(open(DATA_PATH, encoding='utf-8-sig')))
D={r['event_id']:r for r in rows}
ORDER=['WJAPAN2018','HAGIBIS2019','LEKIMA2019','BLACKSUMMER2019','ZHENGZHOU2021',
       'AHR2021','BCHEAT2021','OSONG2023','MAUI2023','VALENCIA2024','BLATTEN2025']
LAB={'WJAPAN2018':'W. Japan 2018','HAGIBIS2019':'Hagibis 2019','LEKIMA2019':'Lekima 2019',
 'BLACKSUMMER2019':'Black Summer 2019–20','ZHENGZHOU2021':'Zhengzhou 2021','AHR2021':'Ahr 2021',
 'BCHEAT2021':'BC heat dome 2021','OSONG2023':'Osong 2023','MAUI2023':'Maui 2023',
 'VALENCIA2024':'Valencia 2024','BLATTEN2025':'Blatten 2025'}
BCOL=['S2','S3','S4\nspec.','S4\nexec.','S4 → S5','Con-\nnected']
PRI={'WJAPAN2018':4,'ZHENGZHOU2021':1,'AHR2021':2,'OSONG2023':3,'MAUI2023':0,'BLATTEN2025':5}
SEC={'ZHENGZHOU2021':3,'MAUI2023':4}

MM=1/25.4
FIG_W=183*MM; FIG_H=150*MM
fig=plt.figure(figsize=(FIG_W,FIG_H))

axa=fig.add_axes([0.215,0.400,0.285,0.520]); axa.set_xlim(0,5); axa.set_ylim(11,0); axa.axis('off')
for j,s in enumerate(['S1','S2','S3','S4','S5']):
    axa.text(j+0.5,-0.22,s,ha='center',va='bottom',fontsize=FS,color=INK)
for i,e in enumerate(ORDER):
    r=D[e]
    axa.text(-0.16,i+0.5,LAB[e],ha='right',va='center',fontsize=FS,color=INK)
    for j,s in enumerate(['S1','S2','S3','S4','S5']):
        st=r[s+'_status']; ex=r.get(s+'_execution_state','')
        fc={'OBSERVED':OBS,'VERIFIED_0':VER,'UNRESOLVED':UNR}[st]
        axa.add_patch(Rectangle((j+0.09,i+0.16),0.82,0.68,facecolor=fc,edgecolor=BORD,lw=LW,zorder=2))
        cx,cy=j+0.5,i+0.5
        if ex=='PARTIAL':
            axa.plot([cx-0.19,cx+0.19],[cy+0.19,cy-0.19],color='black',lw=1.1,solid_capstyle='round',zorder=3)
        elif ex=='NOT_EXECUTED':
            d=0.16
            axa.plot([cx-d,cx+d],[cy-d,cy+d],color='black',lw=1.2,solid_capstyle='round',zorder=3)
            axa.plot([cx-d,cx+d],[cy+d,cy-d],color='black',lw=1.2,solid_capstyle='round',zorder=3)

axb=fig.add_axes([0.560,0.400,0.425,0.520]); axb.set_xlim(0,6); axb.set_ylim(11,0); axb.axis('off')
axb_rx=0.155; axb_ry=axb_rx*(0.425*FIG_W)/(0.520*FIG_H)*(11.0/6.0)
def hm(ax,x,y,rx,ry):
    from matplotlib.patches import Ellipse
    e_=Ellipse((x,y),2*rx,2*ry,facecolor='white',edgecolor=INK,lw=1.1,zorder=4)
    ax.add_patch(e_)
    for k in (-0.62,0.0,0.62):
        ax.plot([x-rx*0.80+k*rx,x+rx*0.80+k*rx],[y+ry*0.80,y-ry*0.80],
                color=INK,lw=1.1,solid_capstyle='butt',zorder=5,clip_path=e_)
for j,h in enumerate(BCOL):
    axb.text(j+0.5,-0.22,h,ha='center',va='bottom',fontsize=FS,color=INK,linespacing=1.30)
for i,e in enumerate(ORDER):
    axb.plot([0.10,5.90],[i+0.5,i+0.5],color='#BFBFBF',lw=1.0,zorder=1)
    if e not in PRI: continue
    p=PRI[e]
    if e in SEC:
        axb.scatter([SEC[e]+0.5],[i+0.5],s=26,c=INK,edgecolors=INK,linewidths=LW,zorder=4)
    if e=='AHR2021':
        hm(axb,p+0.5,i+0.5,axb_rx,axb_ry)
    elif e=='BLATTEN2025':
        axb.scatter([p+0.5],[i+0.5],s=110,facecolors='white',edgecolors=INK,linewidths=1.4,zorder=4)
    else:
        axb.scatter([p+0.5],[i+0.5],s=110,c=INK,edgecolors=INK,linewidths=LW,zorder=4)

axs=fig.add_axes([0.0,0.300,1.0,0.082]); axs.set_xlim(0,183); axs.set_ylim(0,12); axs.axis('off')
axs.text(4.0,7.6,'S1 hazard knowledge · S2 actionable risk information · S3 institutional activation',
         ha='left',va='center',fontsize=FS,color=INK)
axs.text(4.0,1.4,'S4 protective action · S5 actual human protective action · S4 spec. = specification · S4 exec. = execution',
         ha='left',va='center',fontsize=FS,color=INK)

axl=fig.add_axes([0.0,0.012,1.0,0.272]); axl.set_xlim(0,183); axl.set_ylim(0,46); axl.axis('off')
def sw(x,y,fc,txt,slash=False,cross=False):
    axl.add_patch(Rectangle((x,y),8.0,5.4,facecolor=fc,edgecolor=BORD,lw=LW))
    cx,cy=x+4.0,y+2.7
    if slash: axl.plot([cx-2.0,cx+2.0],[cy+2.0,cy-2.0],color='black',lw=1.1,solid_capstyle='round')
    if cross:
        axl.plot([cx-1.7,cx+1.7],[cy-1.7,cy+1.7],color='black',lw=1.2,solid_capstyle='round')
        axl.plot([cx-1.7,cx+1.7],[cy+1.7,cy-1.7],color='black',lw=1.2,solid_capstyle='round')
    axl.text(x+10.8,cy,txt,ha='left',va='center',fontsize=FS,color=INK)
axl.text(4.0,42.0,'Evidence status',ha='left',va='center',fontsize=FS,color=INK,fontweight='bold')
sw(4.0,33.0,OBS,'Observed'); sw(4.0,24.0,VER,'Documented non-execution'); sw(4.0,15.0,UNR,'Unresolved')
axl.text(4.0,10.2,'Execution state',ha='left',va='center',fontsize=FS,color=INK,fontweight='bold')
sw(4.0,1.4,OBS,'Partial',slash=True)
sw(72.0,1.4,VER,'Not executed',cross=True)
axl.text(100.0,42.0,'Break assignment',ha='left',va='center',fontsize=FS,color=INK,fontweight='bold')
axl.scatter([104.0],[35.7],s=110,c=INK,edgecolors=INK,linewidths=LW)
axl.text(110.8,35.7,'Primary discontinuity',ha='left',va='center',fontsize=FS,color=INK)
axl.scatter([104.0],[26.7],s=26,c=INK,edgecolors=INK,linewidths=LW)
axl.text(110.8,26.7,'Secondary discontinuity',ha='left',va='center',fontsize=FS,color=INK)
hm(axl,104.0,17.7,2.6,2.6)
axl.text(110.8,17.7,'Includes secondhand extraction',ha='left',va='center',fontsize=FS,color=INK)
axl.scatter([104.0],[8.7],s=110,facecolors='white',edgecolors=INK,linewidths=1.4)
axl.text(110.8,8.7,'Connected chain (no discontinuity)',ha='left',va='center',fontsize=FS,color=INK)

fig.text(0.020,0.950,'a',fontsize=8,fontweight='bold',color=INK)
fig.text(0.540,0.950,'b',fontsize=8,fontweight='bold',color=INK)

for ext in ['pdf','svg']:
    fig.savefig(f'Fig1_FINAL.{ext}',format=ext,pad_inches=0,transparent=False,facecolor='white')
fig.savefig('Fig1_FINAL_600dpi.png',dpi=600,pad_inches=0,facecolor='white')
t=open('Fig1_FINAL.svg').read().replace('font-family: Helvetica','font-family: Helvetica, Arial, sans-serif')
open('Fig1_FINAL.svg','w').write(t)
print('font used:',FONT)
print('canvas: %.2f x %.2f mm'%(FIG_W/MM,FIG_H/MM))
