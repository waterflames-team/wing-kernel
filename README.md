# lingkong-wing（灵翼）

## 介绍
灵翼是一个由非凡小王开发，折腾调协助维护的基于python3语言的一键建站系统

## 软件架构

### 此仓库
| 仓库   	 |    仓库文件夹	 |
| :--: 	| :--:	 |
| wing.py（主文件） 	| 因不同的主题而异/统一一个（作者还在思考） 	 |
| blog_exhibition（默认主题文件） 	|  	 |
| readme（readme所需的文件） 	|  	 |
| con.py（json读取文件） 	|  	 |
| theme（主题选择文件） 	|  	 |
| LICENSE（开源协议） 	|  	 |
| README(本自述文件) 	|  	 |
### 主题仓库
|   外部  |    内部   |  再内部 |
| :--: 	    | :--:	  |:--:	  |
| 主题1 	| json配置文件 	 |     |
| 主题2 	| 以此类推 	|       |
| 样式文件 	| 主题1 	|   index文件   |
|      |        |    web文件夹（其他web文件）   |



## 系统环境
#### mac、linux和win都可以
#### 手机版可以等一下后面的在线版（有关关键词：github、gitee、在线修改、灵活管理）

## 安装教程
#### 首先你要保证你的电脑中有python3和git（git可选）
#### 如没有可以百度一下属于自己系统的python3和git（git可选）安装方式
#### 作者的python为3.7.3，如果你用你下载的python3运行出现错误，可以试一试使用与作者相同的python3.7.3

1. 把仓库下载下来，然后终端执行：
```
git clone https://gitee.com/lingkonggzs/lingkong-wing.git
```
##### 不想安装git的用户可以下载zip，然后打开cmd，cd到这个目录下，继续操作，但这种方法是不推荐的
2.  cd lingkong-wing
3.  去往[主题仓库](https://gitee.com/lingkonggzs/lingkong-wing-theme.git)选择自己喜欢的主题，放入你的lingkong-wing文件夹内，然后编辑主题名（到时候是以英文呈现）为文件夹名
##### 温馨提示：以上这步可以不做，因为wing有一款自带的主题

#### 然后你的前期的环境准备工作就完成了

## 使用说明
#### 首先你要打开theme.json
#### 把theme这项后面的引号里的blog-XXXX改成你复制过来主题的文件夹名
##### 温馨提示：以上这步可以不做，因为wing有一款自带的主题
#### 然后打开你的主题文件夹，打开文件夹下的config.json配置上你喜欢的东西
### 配置内容说明：
1. `user`:用户称呼
2. `photo`:头像地址（本地与网络上的均可）
2. `word-max`:最大的文章值
2. `word-1\2\3-id`:文章id
2. `word-1\2\3-title`:文章标题
2. `word-1\2\3-date`:文章发表日期
2. `word-1\2\3-content`:文章内容
2. `right-name`:跳转区名字
2. `right-max`:最大的链接数量
2. `right-1\2\3-id`:链接id
2. `right-1\2\3-id`:链接名字
2. `right-1\2\3-id`:链接跳转地址（本地与网络上的均可）

### 如何新建文章：
![第一步](https://gitee.com/lingkonggzs/lingkong-wing/raw/master/readme/1.png)
![第二步](https://gitee.com/lingkonggzs/lingkong-wing/raw/master/readme/2.png)

### 如何新建友链：
![第一步](https://gitee.com/lingkonggzs/lingkong-wing/raw/master/readme/3.png)
![第二步](https://gitee.com/lingkonggzs/lingkong-wing/raw/master/readme/4.png)

## 以下是几个常用的命令
1.  `python3 wing.py`:查看介绍
2.  `python3 wing.py s`:激活配置生效
3.  `python3 wing.py z`:查看使用指南
3.  `python3 wing.py v`:查看版本号


## 参与贡献

1.  直接修改代码
2.  提交代码
3.  申请 Pull Request
#### 如果要投稿主题，还可以
1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request

> 以上内容均为项目设计

## 错误说明
#### 如果你运行时出现错误
#### 请尝试以下方法：
1. 确认是否是按照作者的方法一步一步做的
2. 确认编辑config.json的格式是否错误
#### 如果以上办法无效，请划到最下面联系作者

## 版本号说明
#### 版本号的定义为：主版本号.可使用主题数.主程序更新次数-最后更新时间
#### 如：
##### 0.1.34-200425
##### =
##### 第0个主版本，1个可以使用的主题，主程序已更新34次，最后更新时间为2020年4月25日

## 在线版预告
#### 手机用户可以等一等未来会开发的在线版
#### 在线版在一个网页上，支持本地端的所有功能
#### 还支持一键同步github、gitee
#### 敬请期待!!!

## 前线开发状态

#### 开发协作群开发主题中：[跳转仓库](https://gitee.com/lingkonggzs/lingkong-wing-theme.git)

#### 已适配好默认主题

## 作者联系方式
> 如果你有问题，请你通过以下方式联系非凡小王（作者）

* 作者钉钉：15392006285（加好友请说明来历）

* 作者qq：2822603942（加好友请说明来历）