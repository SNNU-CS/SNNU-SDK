'''
Created on Dec 29, 2018

@author: QiZhao
'''
SPIDER_CONFIG = [
    {
        'department_EN': 'snnu_index',
        'department_CN': '学校主页',
        'url': 'http://www.snnu.edu.cn/tzgg.htm',
        'url_main': 'http://www.snnu.edu.cn/info/1085/',
        'rule': 'info/1085/(?P<link>\d+\.htm)" target="_blank">(?P<title>[\s\S]{5,100})（(?P<date>\d*-\d*-\d*)）',
        'coding': 'utf-8',
        'type': '通知'
    },
    {
        'department_EN': 'snnu_index',
        'department_CN': '学校主页',
        'url': 'http://www.snnu.edu.cn/sdxw.htm',
        'url_main': 'http://www.snnu.edu.cn/info/1084/',
        'rule': 'info/1084/(?P<link>\d+.htm)" target="_blank" title="(?P<title>[^"]+?)"><[^<]+?<[^<]+?<[^<]+?<p class="qh-wide-pushtime">(?P<date>\d*-\d*-\d*)',
        'coding': 'utf-8',
        'type': '新闻' 
    },
    {
        'department_EN': 'snnu_css',
        'department_CN': '计算机科学学院',
        'url': 'http://ccs.snnu.edu.cn/tzgg.htm',
        'url_main': 'http://ccs.snnu.edu.cn/',
        'rule': '<a target="_blank" href="(?P<link>[^"]*)">(?P<title>[^<]*)<[^"]*"[^>]*>(?P<date>\d*-\d*-\d*)',
        'coding': 'utf-8',
        'type': '通知'
    },
    {
        'department_EN': 'snnu_css',
        'department_CN': '计算机科学学院',
        'url': 'http://ccs.snnu.edu.cn/xydt.htm',
        'url_main': 'http://ccs.snnu.edu.cn/',
        'rule': '<a target="_blank" href="(?P<link>[^"]*)">(?P<title>[^<]*?)<[^"]*"[^>]*>(?P<date>\d*-\d*-\d*)',
        'coding': 'utf-8',
        'type': '新闻'
    },
    {
        'department_EN': 'snnu_jwc',
        'department_CN': '教务处',
        'url': 'http://jwc.snnu.edu.cn/news_more.xhm?lm=2',
        'url_main': 'http://jwc.snnu.edu.cn/html/news_view.xhm?newsid=',
        'rule': 'newsid=(?P<link>\d*)" [^ ]* title="(?P<title>[^(">)]*)[^<]*[^(]*\((?P<date>\d*/\d*/\d*)',
        'coding': 'gbk',
        'type': '通知'
    },
    {
        'department_EN': 'snnu_jwc',
        'department_CN': '教务处',
        'url': 'http://jwc.snnu.edu.cn/news_more.xhm?lm=1',
        'url_main': 'http://jwc.snnu.edu.cn/html/news_view.xhm?newsid=',
        'rule': 'newsid=(?P<link>\d*)" [^ ]* title="(?P<title>[^(">)]*)[^<]*[^(]*\((?P<date>\d*/\d*/\d*)',
        'coding': 'gbk',
        'type': '新闻'
    },
    {
        'department_EN': 'snnu_xsc',
        'department_CN': '学生处',
        'url': 'http://www.xsc.snnu.edu.cn/Announcements.asp',
        'url_main': 'http://www.xsc.snnu.edu.cn/Announcements.asp?id=144&bh=',
        'rule': 'gk3">(?P<date>\d*-\d*-\d*)[^;]*;[^;]*;[^;]*;[^;]*;bh=(?P<link>\d*)[^>]*>(?P<title>[^</]*)',
        'coding': 'gbk',
        'type': '通知'
    },
    {
        'department_EN': 'snnu_xsc',
        'department_CN': '学生处',
        'url': 'http://www.xsc.snnu.edu.cn/News.asp',
        'url_main': 'http://www.xsc.snnu.edu.cn/News.asp?id=159&bh=',
        'rule': 'gk3">(?P<date>\d*-\d*-\d*)[^;]*;[^;]*;[^;]*;[^;]*;bh=(?P<link>\d*)[^>]*>(?P<title>[^</]*)',
        'coding': 'gbk',
        'type': '新闻'
    },
    {
        'department_EN': 'snnu_lib',
        'department_CN': '图书馆',
        'url': 'http://www.lib.snnu.edu.cn/action.do?webid=w-d-bggg-l',
        'url_main': 'http://www.lib.snnu.edu.cn/action.do?webid=w-l-showmsg&gtype=a&pid=',
        'rule': 'pid=(?P<link>\d*)[\s\S]{20,57}>(?P<title>[^<]*)</[af][\S\s]{18,70}(?P<date>\d{4}-\d*-\d*)',
        'coding': 'utf-8',
        'type':'通知'
    },
    {
        'department_EN': 'snnu_lib',
        'department_CN': '图书馆',
        'url': 'http://www.lib.snnu.edu.cn/action.do?webid=w-d-bgxw-l',
        'url_main': 'http://www.lib.snnu.edu.cn/action.do?webid=w-l-showmsg&gtype=a&pid=',
        'rule': 'pid=(?P<link>\d*)[\s\S]{20,57}>(?P<title>[^<]*)</[af][\S\s]{18,70}(?P<date>\d{4}-\d*-\d*)',
        'coding': 'utf-8',
        'type':'新闻'
    },
    {
        'department_EN': 'snnu_clxy',
        'department_CN': '材料科学与工程学院',
        'url': 'http://clxy.snnu.edu.cn/home/list/?bh=008',
        'url_main': 'http://clxy.snnu.edu.cn/Home/show/',
        'rule': 'show[/](?P<link>\d*)"[\s\S]{1,}?"(?P<title>[\s\S]{1,}?)"[^<]{1,}?</a>[\S\s]{1,200}<td align="center">[^\d]*(?P<date>\d*-\d*-\d*)',
        'coding': 'utf-8',
        'type': '通知'
    },
    {
        'department_EN': 'snnu_clxy',
        'department_CN': '材料科学与工程学院',
        'url': 'http://clxy.snnu.edu.cn/home/list/?bh=009',
        'url_main': 'http://clxy.snnu.edu.cn/Home/show/',
        'rule': 'show[/](?P<link>\d*)"[\s\S]{1,}?"(?P<title>[\s\S]{1,}?)"[^<]{1,}?</a>[\S\s]{1,200}<td align="center">[^\d]*(?P<date>\d*-\d*-\d*)',
        'coding': 'utf-8',
        'type': '新闻'
    },
    {
        'department_EN': 'snnu_marxism',
        'department_CN': '马克思主义学院',
        'url': 'http://marxism.snnu.edu.cn/tzgg/tzgg.htm',
        'url_main': 'http://marxism.snnu.edu.cn/info/1062/',
        'rule': 'class="fr">(?P<date>\d*-\d*-\d*)</span>[\s]+?<a href="../info/1062/(?P<link>\d+.htm)" target="_blank" title="(?P<title>[^"]+?)">',
        'coding': 'utf-8',
        'type': '通知' 
    },
    {
        'department_EN': 'snnu_marxism',
        'department_CN': '马克思主义学院',
        'url': 'http://marxism.snnu.edu.cn/xyxw/xyxw.htm',
        'url_main': 'http://marxism.snnu.edu.cn/info/1062/',
        'rule': 'href="../info/1061/(?P<link>\d+.htm)" target="_blank" title="(?P<title>[^"]+?)">[\S]+[\s]+?<h2>(?P<date>\d*-\d*-\d*)<',
        'coding': 'utf-8',
        'type': '新闻' 
    },
    {
        'department_EN': 'snnu_lit',
        'department_CN': '文学院',
        'url': 'http://www.lit.snnu.edu.cn/index.php?m=content&c=index&a=lists&catid=62',
        'url_main': 'http://www.lit.snnu.edu.cn/index.php?m=content&c=index&a=show&catid=',
        'rule': 'show&catid=(?P<link>\d*&id=\d*)[\s\S]+?title">(?P<title>[^<]*)<[\s\S]+?date2">(?P<date>\d*-\d*-\d*)',
        'coding': 'utf-8',
        'type': '通知' 
    },
    {
        'department_EN': 'snnu_lit',
        'department_CN': '文学院',
        'url': 'http://www.lit.snnu.edu.cn/index.php?m=content&c=index&a=lists&catid=9',
        'url_main': 'http://www.lit.snnu.edu.cn/index.php?m=content&c=index&a=show&catid=',
        'rule': 'show&catid=(?P<link>\d*&id=\d*)[\s\S]+?title">(?P<title>[^<]*)<[\s\S]+?date2">(?P<date>\d*-\d*-\d*)',
        'coding': 'utf-8',
        'type': '新闻' 
    },
    {
        'department_EN': 'snnu_his',
        'department_CN': '历史文化学院',
        'url': 'http://his.snnu.edu.cn/notice.asp',
        'url_main': 'http://his.snnu.edu.cn/notice.asp?id=',
        'rule': 'notice.asp[?]id=(?P<link>\d*)">(?P<title>[^<]*)[^\[]*\[(?P<date>\d*/\d*/\d*)',
        'coding': 'utf-8',
        'type': '通知' 
    },
    {
        'department_EN': 'snnu_his',
        'department_CN': '历史文化学院',
        'url': 'http://his.snnu.edu.cn/news.asp',
        'url_main': 'http://his.snnu.edu.cn/news.asp?id=',
        'rule': 'news.asp[?]id=(?P<link>\d*)">(?P<title>[^<]*)[^\[]*\[(?P<date>\d*/\d*/\d*)',
        'coding': 'utf-8',
        'type': '新闻' 
    },
    {
        'department_EN': 'snnu_se',
        'department_CN': '教育学院',
        'url': 'http://se.snnu.edu.cn/news.php?cat_id=1342',
        'url_main': 'http://se.snnu.edu.cn/news_detail.php?id=',
        'rule': 'php[?]id=(?P<link>\d*)">(?P<title>[^（]*)（(?P<date>\d*-\d*-\d*)',
        'coding': 'utf-8',
        'type': '通知' 
    },
    {
        'department_EN': 'snnu_se',
        'department_CN': '教育学院',
        'url': 'http://se.snnu.edu.cn/news.php?cat_id=1341',
        'url_main': 'http://se.snnu.edu.cn/news_detail.php?id=',
        'rule': 'php[?]id=(?P<link>\d*)">(?P<title>[^（]*)（(?P<date>\d*-\d*-\d*)',
        'coding': 'utf-8',
        'type': '新闻' 
    },
    {
        'department_EN': 'snnu_psych',
        'department_CN': '心理学院',
        'url': 'http://psych.snnu.edu.cn/home/list/?bh=008',
        'url_main': 'http://psych.snnu.edu.cn/home/show/',
        'rule': 'show/(?P<link>\d*)[^>]+?>(?P<title>[^ ]*)[\S\s]+?<td align=[\s\S]+?(?P<date>\d*-\d*-\d*)',
        'coding': 'utf-8',
        'type': '通知' 
    },
    {
        'department_EN': 'snnu_psych',
        'department_CN': '心理学院',
        'url': 'http://psych.snnu.edu.cn/home/list/?bh=009',
        'url_main': 'http://psych.snnu.edu.cn/home/show/',
        'rule': 'show/(?P<link>\d*)[^>]+?>(?P<title>[^ ]*)[\S\s]+?<td align=[\s\S]+?(?P<date>\d*-\d*-\d*)',
        'coding': 'utf-8',
        'type': '新闻' 
    },
    {
        'department_EN': 'snnu_wyxy',
        'department_CN': '外国语学院',
        'url': 'http://www.wyxy.snnu.edu.cn/wenzi_list.jsp?urltype=tree.TreeTempUrl&wbtreeid=1044',
        'url_main': 'http://www.wyxy.snnu.edu.cn/info/1044/',
        'rule': 'info/1044/(?P<link>\d+.htm)" title="" class="left">(?P<title>\S{4,100})</a><span class="right">(?P<date>\d*-\d*-\d*)<',
        'coding': 'utf-8',
        'type': '通知' 
    },
    {
        'department_EN': 'snnu_wyxy',
        'department_CN': '外国语学院',
        'url': 'http://www.wyxy.snnu.edu.cn/wenzi_list.jsp?urltype=tree.TreeTempUrl&wbtreeid=1043',
        'url_main': 'http://www.wyxy.snnu.edu.cn/info/1043/',
        'rule': 'info/1043/(?P<link>\d+.htm)" title="" class="left">(?P<title>\S{4,100})</a><span class="right">(?P<date>\d*-\d*-\d*)<',
        'coding': 'utf-8',
        'type': '新闻' 
    },
    {
        'department_EN': 'snnu_maths',
        'department_CN': '数学与信息科学学院',
        'url': 'http://maths.snnu.edu.cn/ggtz.htm',
        'url_main': 'http://maths.snnu.edu.cn/info/1041/',
        'rule': '1041/(?P<link>\d*.htm)">[\s\S]{18}(?P<title>[^ ]+)[ ]{5,}[^[]+?[^\d]+?(?P<date>\d+-\d+-\d+)',
        'coding': 'utf-8',
        'type': '通知' 
    },
    {
        'department_EN': 'snnu_maths',
        'department_CN': '数学与信息科学学院',
        'url': 'http://maths.snnu.edu.cn/xyxw.htm',
        'url_main': 'http://maths.snnu.edu.cn/info/1042/',
        'rule': '1042/(?P<link>\d*.htm)">[\s\S]{18}(?P<title>[^ ]+)[ ]{5,}[^[]+?[^\d]+?(?P<date>\d+-\d+-\d+)',
        'coding': 'utf-8',
        'type': '新闻' 
    },
    {
        'department_EN': 'snnu_wuli',
        'department_CN': '物理学与信息技术学院',
        'url': 'http://wuli.snnu.edu.cn/home/list/12',
        'url_main': 'http://wuli.snnu.edu.cn/home/content/',
        'rule': 'content/(?P<link>\d+)" title="(?P<title>[^"]*)[^<]+?</a>[^>]+?>(?P<date>\d*-\d*-\d*)',
        'coding': 'utf-8',
        'type': '通知' 
    },
    {
        'department_EN': 'snnu_wuli',
        'department_CN': '物理学与信息技术学院',
        'url': 'http://wuli.snnu.edu.cn/home/list/11',
        'url_main': 'http://wuli.snnu.edu.cn/home/content/',
        'rule': 'content/(?P<link>\d+)" title="(?P<title>[^"]*)[^<]+?</a>[^>]+?>(?P<date>\d*-\d*-\d*)',
        'coding': 'utf-8',
        'type': '新闻' 
    },
    {
        'department_EN': 'snnu_spg',
        'department_CN': '哲学与政府管理学院',
        'url': 'http://spg.snnu.edu.cn/Notice.asp',
        'url_main': 'http://spg.snnu.edu.cn/Notice.asp?id=32&bh=',
        'rule': 'bh=(?P<link>\d+)[^>]+?>(?P<title>[^<]+?)<[^;]+?;[^;]+?;">(?P<date>\d+-\d+-\d+)',
        'coding': 'gbk',
        'type': '通知' 
    },
    {
        'department_EN': 'snnu_spg',
        'department_CN': '哲学与政府管理学院',
        'url': 'http://spg.snnu.edu.cn/College_News.asp',
        'url_main': 'http://spg.snnu.edu.cn/College_News.asp?id=31&bh=',
        'rule': 'bh=(?P<link>\d+)[^>]+?>(?P<title>[^<]+?)<[^;]+?;[^;]+?;">(?P<date>\d+-\d+-\d+)',
        'coding': 'gbk',
        'type': '新闻' 
    },
    {
        'department_EN': 'snnu_chem',
        'department_CN': '化学化工学院',
        'url': 'http://www.chem.snnu.edu.cn/wenzi_list.aspx?category_id=19',
        'url_main': 'http://www.chem.snnu.edu.cn/neiye_show.aspx?id=',
        'rule': 'aspx[?]id=(?P<link>\d*)">(?P<title>[^<]*)<[\S\s]{1,45}(?P<date>\d{4}-\d{2}-\d{2})',
        'coding': 'utf-8',
        'type': '通知' 
    },
    {
        'department_EN': 'snnu_chem',
        'department_CN': '化学化工学院',
        'url': 'http://www.chem.snnu.edu.cn/wenzi_list.aspx?category_id=20',
        'url_main': 'http://www.chem.snnu.edu.cn/neiye_show.aspx?id=',
        'rule': 'aspx[?]id=(?P<link>\d*)">(?P<title>[^<]*)<[\S\s]{1,45}(?P<date>\d{4}-\d{2}-\d{2})',
        'coding': 'utf-8',
        'type': '新闻' 
    },
    {
        'department_EN': 'snnu_lifesci',
        'department_CN': '生命科学学院',
        'url': 'http://lifesci.snnu.edu.cn/listall.aspx?Index_code=tzgg',
        'url_main': 'http://lifesci.snnu.edu.cn/inforshow.aspx?id=',
        'rule': 'aspx[?]id=(?P<link>\d*)">(?P<title>[^<]*)</a></li>[^>]*>(?P<date>\d*-\d*-\d*)</li>',
        'coding': 'utf-8',
        'type': '通知' 
    },
    {
        'department_EN': 'snnu_lifesci',
        'department_CN': '生命科学学院',
        'url': 'http://lifesci.snnu.edu.cn/listall.aspx?Index_code=xydt',
        'url_main': 'http://lifesci.snnu.edu.cn/inforshow.aspx?id=',
        'rule': 'aspx[?]id=(?P<link>\d*)">(?P<title>[^<]*)</a></li>[^>]*>(?P<date>\d*-\d*-\d*)</li>',
        'coding': 'utf-8',
        'type': '新闻' 
    },
    {
        'department_EN': 'snnu_geog',
        'department_CN': '地理科学与旅游学院',
        'url': 'http://geog.snnu.edu.cn/news.jsp?urltype=tree.TreeTempUrl&wbtreeid=1020',
        'url_main': 'http://geog.snnu.edu.cn/info/1020/',
        'rule': '<span class="fr">(?P<date>\d{4}-\d{2}-\d{2})<[^"]{1,100}"info/1020/(?P<link>\d*.htm)">(?P<title>[^<]*)<',
        'coding': 'utf-8',
        'type': '通知' 
    },
    {
        'department_EN': 'snnu_geog',
        'department_CN': '地理科学与旅游学院',
        'url': 'http://geog.snnu.edu.cn/news.jsp?urltype=tree.TreeTempUrl&wbtreeid=1019',
        'url_main': 'http://geog.snnu.edu.cn/info/1019/',
        'rule': '<span class="fr">(?P<date>\d{4}-\d{2}-\d{2})<[^"]{1,100}"info/1019/(?P<link>\d*.htm)">(?P<title>[^<]*)<',
        'coding': 'utf-8',
        'type': '新闻' 
    },
    {
        'department_EN': 'snnu_cxinw',
        'department_CN': '新闻与传播学院',
        'url': 'http://cxinw.snnu.edu.cn/News_bulletin.asp?id=15',
        'url_main': 'http://cxinw.snnu.edu.cn/News_bulletin.asp?id=15&bh=',
        'rule': 'bh=(?P<link>\d*)" class="c5">(?P<title>[^<]*)</a>[\s\S]{1,100}<span class="gk3">(?P<date>\d*-\d*-\d*)<',
        'coding': 'gbk',
        'type': '通知' 
    },
    {
        'department_EN': 'snnu_cxinw',
        'department_CN': '新闻与传播学院',
        'url': 'http://cxinw.snnu.edu.cn/News_bulletin.asp?id=14',
        'url_main': 'http://cxinw.snnu.edu.cn/News_bulletin.asp?id=14&bh=',
        'rule': 'bh=(?P<link>\d*)" class="c5">(?P<title>[^<]*)</a>[\s\S]{1,100}<span class="gk3">(?P<date>\d*-\d*-\d*)<',
        'coding': 'gbk',
        'type': '新闻' 
    },
    {
        'department_EN': 'snnu_tyxy',
        'department_CN': '体育学院',
        'url': 'http://tyxy.snnu.edu.cn/Notice.asp',
        'url_main': 'http://tyxy.snnu.edu.cn/Notice.asp?id=34&bh=',
        'rule': 'font-weight:normal;">(?P<date>\d*-\d*-\d*)</span></td>[^&]+?&nbsp;/&nbsp;&nbsp;&nbsp;<a href="/News_information.asp[?]id=33&amp;bh=(?P<link>\d*)">\r\n(?P<title>[^\r]*?)\r\n',
        'coding': 'gbk',
        'type': '通知' 
    },
    {
        'department_EN': 'snnu_tyxy',
        'department_CN': '体育学院',
        'url': 'http://tyxy.snnu.edu.cn/News_information.asp',
        'url_main': 'http://tyxy.snnu.edu.cn/News_information.asp?id=33&bh=',
        'rule': 'font-weight:normal;">(?P<date>\d*-\d*-\d*)</span></td>[^&]+?&nbsp;/&nbsp;&nbsp;&nbsp;<a href="/News_information.asp[?]id=33&amp;bh=(?P<link>\d*)">\r\n(?P<title>[^\r]*?)\r\n',
        'coding': 'gbk',
        'type': '新闻' 
    },
    {
        'department_EN': 'snnu_music',
        'department_CN': '音乐学院',
        'url': 'http://music.snnu.edu.cn/xwzx/tzgg.htm',
        'url_main': 'http://music.snnu.edu.cn/info/1018/',
        'rule': '<span class="fr">(?P<date>\d{4}-\d{2}-\d{2})<[^\d]{1,50}1018/(?P<link>\d*.htm)">(?P<title>[^<]*)<',
        'coding': 'utf-8',
        'type': '通知' 
    },
    {
        'department_EN': 'snnu_music',
        'department_CN': '音乐学院',
        'url': 'http://music.snnu.edu.cn/xwzx/xyxw.htm',
        'url_main': 'http://music.snnu.edu.cn/info/1017/',
        'rule': '<span class="fr">(?P<date>\d{4}-\d{2}-\d{2})<[^\d]{1,50}1017/(?P<link>\d*.htm)">(?P<title>[^<]*)<',
        'coding': 'utf-8',
        'type': '新闻' 
    },
    {
        'department_EN': 'snnu_meishuxy',
        'department_CN': '美术学院',
        'url': 'http://meishuxy.snnu.edu.cn/News_Center.asp?id=15',
        'url_main': 'http://meishuxy.snnu.edu.cn/News_Center.asp?id=15&bh=',
        'rule': 'bh=(?P<link>\d*)" class="c5">(?P<title>[^<]*)</a>[\s\S]{1,160}>(?P<date>\d*-\d*-\d*)<',
        'coding': 'gbk',
        'type': '通知' 
    },
    {
        'department_EN': 'snnu_meishuxy',
        'department_CN': '美术学院',
        'url': 'http://meishuxy.snnu.edu.cn/News_Center.asp?id=14',
        'url_main': 'http://meishuxy.snnu.edu.cn/News_Center.asp?id=14&bh=',
        'rule': 'bh=(?P<link>\d*)" class="c5">(?P<title>[^<]*)</a>[\s\S]{1,160}>(?P<date>\d*-\d*-\d*)<',
        'coding': 'gbk',
        'type': '新闻' 
    },
    {
        'department_EN': 'snnu_ibs',
        'department_CN': '国际商学院',
        'url': 'http://www.ibs.snnu.edu.cn/Announcements.asp',
        'url_main': 'http://www.ibs.snnu.edu.cn/Announcements.asp?id=18&bh=',
        'rule': 'bh=(?P<link>\d*)" class="c5">(?P<title>[^<]*)</a>[\s\S]{1,150}>\[(?P<date>\d*-\d*-\d*)\]',
        'coding': 'gbk',
        'type': '通知' 
    },
    {
        'department_EN': 'snnu_ibs',
        'department_CN': '国际商学院',
        'url': 'http://www.ibs.snnu.edu.cn/News.asp',
        'url_main': 'http://www.ibs.snnu.edu.cn/Announcements.asp?id=16&bh=',
        'rule': 'bh=(?P<link>\d*)" class="c5">(?P<title>[^<]*)</a>[\s\S]{1,150}>\[(?P<date>\d*-\d*-\d*)\]',
        'coding': 'gbk',
        'type': '新闻' 
    },
    {
        'department_EN': 'snnu_iscs',
        'department_CN': '国际汉学院',
        'url': 'http://iscs.snnu.edu.cn/xwdt/xygg.htm',
        'url_main': 'http://iscs.snnu.edu.cn/info/1132/',
        'rule': '1132[/](?P<link>\d*.htm)"[^>]*>(?P<title>[^<]*)</a>[\s\S]{1,80}>(?P<date>\d*-\d*-\d*) <',
        'coding': 'utf-8',
        'type': '通知' 
    },
    {
        'department_EN': 'snnu_iscs',
        'department_CN': '国际汉学院',
        'url': 'http://iscs.snnu.edu.cn/xwdt/zhyw.htm',
        'url_main': 'http://iscs.snnu.edu.cn/info/1133/',
        'rule': '1133[/](?P<link>\d*.htm)"[^>]*>(?P<title>[^<]*)</a>[\s\S]{1,80}>(?P<date>\d*-\d*-\d*) <',
        'coding': 'utf-8',
        'type': '新闻' 
    },
    {
        'department_EN': 'snnu_spgcx',
        'department_CN': '食品工程与营养科学学院',
        'url': 'http://spgcx.snnu.edu.cn/xwdt/tzgg.htm',
        'url_main': 'http://spgcx.snnu.edu.cn/info/1193/',
        'rule': 'class="fr">(?P<date>\d*-\d*)</span><a href="../info/1193/(?P<link>\d*.htm)" target="_blank" title="(?P<title>[^"]*?)"',
        'coding': 'utf-8',
        'type': '通知' 
    },
    {
        'department_EN': 'snnu_spgcx',
        'department_CN': '食品工程与营养科学学院',
        'url': 'http://spgcx.snnu.edu.cn/xwdt/xyxw.htm',
        'url_main': 'http://spgcx.snnu.edu.cn/info/1192/',
        'rule': 'class="fr">(?P<date>\d*-\d*)</span><a href="../info/1192/(?P<link>\d*.htm)" target="_blank" title="(?P<title>[^"]*?)"',
        'coding': 'utf-8',
        'type': '新闻' 
    }
]