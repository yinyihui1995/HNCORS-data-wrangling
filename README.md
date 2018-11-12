# HNCORS-data-wrangling / 湖南 CORS 数据整理
Decompression, splicing, renaming and classification of HNCORS data files.

对 HNCORS 的数据文件进行解压缩、拼接、重命名和分类操作。

## Implementation of features / 功能的实现
Realization / 实现情况 | features / 功能
--------- | -------------
✔︎ | Decompression / 观测文件的解压缩
✘ | Splice / 观测文件的拼接
✘ | Rename / 观测文件的重命名
✘ | Classification / 观测文件的分类归档

## Directory structure of data files / 数据文件的目录结构

目录大致结构：
```
├─001
│  ├─CD**
│  │  └─CD**001aB.zip
│  ⋮
│  ├─YZ**
│  │  └─YZ**0010.17d.zip
│  ⋮
│  ├─HH**
│  │  ├─HH**001tB.zip
│  │  ├─HH**001aB.zip
│  │  ⋮
│  │  └─HH**001bB.zip
│  ⋮
│  ├─SY**
│  │  └─SY**0010.17o.zip
│  ⋮
│  ├─HH**
│  │  ├─HH**0010.17d.zip
│  │  ├─HH**001q31.17d.zip
│  │  ⋮
│  │  └─HH**001x15.17d.zip
│  ⋮
│  ├─SY**
│  │  ├─SY**001n25.17o.zip
│  │  ⋮
│  │  └─SY**001u12.17o.zip
│  ⋮
│  └─****
├─002
│  ├─CD**
│  ⋮
│  └─****
⋮
└─365
   ├─CD**
   ⋮
   └─****
```