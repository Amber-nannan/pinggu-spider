# 经管之家爬虫
从[经管之家](https://bbs.pinggu.org/)爬取与经管知识相关的问答数据。

## [经管爱问](https://ask.pinggu.org/?c-all/all)
共计约66万个问题，每个问题包含：标题、标签、回答/浏览数量，以及时间。

## [经管之家](https://bbs.pinggu.org/)
经管之家中所有的帖子可以通过统一的格式访问
- Base URL: https://bbs.pinggu.org/forum.php
- Key Words:
    - mod: viewthread
    - tid: TID, 对应帖子的id
    - page: PAGE, 需要查看的页数
- Request URL: https://bbs.pinggu.org/forum.php?mod=viewthread&tid=1&page=1

或者：
- https://bbs.pinggu.org/thread-TID-PAGE-1.html
- 其中TID以及PAGE定义同上

### [经管百科](https://bbs.pinggu.org/forum-4104-1.html)
包含若干子版块，具体内容如下
- [爱问频道](https://bbs.pinggu.org/forum-139-1.html): 
无所不问，有问共答。生活上，学术上，职场上，想问就问。互助解决经济、管理、金融、统计及考研、财经类各种问题

- [经管百科·经济学](https://bbs.pinggu.org/forum-3870-1.html)
- [经管百科·管理学](https://bbs.pinggu.org/forum-3871-1.html)
- [经管百科·金融学](https://bbs.pinggu.org/forum-3874-1.html)
- [经管百科·会计学](https://bbs.pinggu.org/forum-3875-1.html)
- [经管百科·统计学](https://bbs.pinggu.org/forum-3873-1.html)
- [经管百科·国经贸](https://bbs.pinggu.org/forum-3876-1.html)