import os,sys,markdown,re
from natsort import natsorted, ns
l={}
pa=sys.path[0]
for a in os.walk(pa):
    if'/.git'in a[0]:
        continue
    if a[0]in l:
        continue
    f=['%s/%s'%(a[0],c)for c in os.listdir(a[0])if(c[0]!='.')and('index.htm'not in c)]
    d=[c for c in f if os.path.isdir(c)]
    fi=[c for c in f if c not in d]
    d=natsorted(d,alg=ns.IGNORECASE)
    fi=natsorted(fi,alg=ns.IGNORECASE)
    l[a[0]]=[d,fi]
pl=repr(l)
pl='%s……%s'%(pl[:512],pl[-512:])
print(pl)
lp=len(pa)
foi='''<svg aria-label="Directory" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file-directory-fill hx_color-icon-directory"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg>'''
fii='''<svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg>'''
ht='''<html>
<head>
<style>a:link{color:#000000;text-decoration:none}a:hover{color:#0645ad;text-decoration:underline;}</style>
</head>
<body>
<svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo color-fg-muted mr-2">
<path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>    
<span class="author flex-self-stretch" itemprop="author">
<a class="url fn" rel="author" data-hovercard-type="user" data-hovercard-url="/users/banned-historical-archives/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/banned-historical-archives">
banned-historical-archives</a></span>
<span class="mx-1 flex-self-stretch color-fg-muted">/</span>
<strong itemprop="name" class="mr-2 flex-self-stretch">
<a data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="<!--INDEX.HTM-->">CCRD</a>
</strong>
<span></span>
<span class="Label Label--secondary v-align-middle mr-1">Public</span>
<span></span>
%s<a href='<!--FPRL.TXT-->' download>Fast Pure Raw Links.txt</a>
<!--LOAD PATH-->
<hr>
<!--LOAD LIST-->
<hr>
<!--LOAD MD-->
</body></html>'''%fii
pp=sys.path[0]
f=open('README.md','r');t=f.read();f.close()
md=markdown.markdown(t)
lp2=len('/'.join(sys.path[0].split('/')[:-1]))
lpp=len(pp)
for a in l.keys():
    if not os.path.exists(rl:='%s/%s'%(pp,a[lp+1:]))and a!=pa:os.makedirs(rl)
    if a==pa:
        la=l[a]
        li=[]
        for b in la[0]:
            li.append('%s <a href="./%s/index.htm">%s</a>'%(foi,b[lp+1:],b.split('/')[-1]))
        for b in la[1]:
            li.append('%s <a href="%s">%s</a>'%(fii,b[lp+1:].split('/')[-1],b.split('/')[-1]))
        li='\n<br>\n'.join(li)
        ht2=ht.replace('<!--LOAD LIST-->',li)
        ht2=ht2.replace('\n<!--LOAD PATH-->','')
        ht2=ht2.replace('<!--INDEX.HTM-->','index.htm')
        ht2=ht2.replace('<!--FPRL.TXT-->','Fast Pure Raw Links.txt')
        ht2=ht2.replace('<!--LOAD MD-->',md)
        print(a)
        f=open('index.htm','w+');f.write(ht2);f.close()
    else:
        la=l[a]
        li=['<a rel="nofollow" title="Go to parent directory" class="js-navigation-open d-block py-2 px-3" href="../index.htm"><span class="text-bold text-center d-inline-block" style="min-width: 16px;">. .</span></a>']
        for b in la[0]:
            pr=len(a[lp+1:].split('/'))
            af=b[lp+1:].split('/')[pr]
            li.append('%s <a href="%s/index.htm">%s</a>'%(foi,af,b.split('/')[-1]))
        for b in la[1]:
            li.append('%s <a href="%s">%s</a>'%(fii,b[lp+1:].split('/')[-1],b.split('/')[-1]))
        li='\n<br>\n'.join(li)
        ht2=ht.replace('<!--LOAD LIST-->',li)
        pr='/'.join(['..'for b in range(len(a[lp+1:].split('/')))])
        ht2=ht2.replace('<!--INDEX.HTM-->','%s/index.htm'%pr)
        ht2=ht2.replace('<!--FPRL.TXT-->','%s/Fast Pure Raw Links.txt'%pr)
        pas=a[lp+1:].split('/')
        lpas=len(pas)
        t=['<span class="js-repo-root text-bold"><span class="js-path-segment d-inline-block wb-break-all"><a data-turbo-frame="repo-content-turbo-frame" href="%s/index.htm"><span>CCRD</span></a></span></span>'%'/'.join(['..'for b in range(lpas)])]
        fn=a[lp+1:].split('/')
        for b in range(lpas):
            if b!=lpas-1:
                t.append('<span class="js-path-segment d-inline-block wb-break-all"><a data-turbo-frame="repo-content-turbo-frame" href="%s/index.htm"><span>%s</span></a></span>'%('/'.join(['..'for b in range(lpas-b-1)]),fn[:-1][b]))
        t.append('<strong class="final-path">%s</strong><span class="mx-1">/</span>'%a.split('/')[-1])
        t='\n<span class="mx-1">/</span>\n'.join(t)
        ht2=ht2.replace('<!--LOAD PATH-->','<hr>\n%s'%t)
        ht2=ht2.replace('<!--LOAD MD-->',md)
        print(a)
        f=open('%s/index.htm'%(a[lp+1:]),'w+');f.write(ht2);f.close()
l2=[]
for a in l.keys():
    l2.extend([b[lp+1:]for b in l[a][1]])
l2=natsorted(l2,alg=ns.IGNORECASE)
l2='\n'.join(l2)
print('end')
f=open('Fast Pure Raw Links.txt','w+');f.write(l2);f.close()
