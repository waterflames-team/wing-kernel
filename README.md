# lingkong-wing（灵翼）

## 介绍
灵翼是一个由非凡小王开发，折腾调协助维护的基于python3语言的一键建站系统

## 软件架构

### 此仓库
| 仓库   	 |    仓库文件夹	 |
| :--: 	| :--:	 |
| wing.py（主文件） 	| blog_exhibition（默认主题文件）	 |
|  	| blog_exhibition：config（内容配置文件）、theme（主题模板文件以及激活文件）	 |
| readme（readme所需的文件） 	|  	 |
| con.py（json读取文件） 	|  	 |
| theme（主题选择文件） 	|  	 |
| LICENSE（开源协议） 	|  	 |
| README(本自述文件) 	|  	 |
### 主题仓库
|   外部  |    内部   |  再内部 |
| :--: 	    | :--:	  |:--:	  |
| 主题1 	| json配置文件 	 |     |
|  	| theme文件 	 |     |
| 主题2 	| 以此类推 	|       |
| 样式文件 	| 主题1 	|   index文件   |
|      |        |    web文件夹（其他web文件）   |

## 效果
#### 欢迎前往[首批测试点（Leo韩）](https://leo-blog.github.io/)查看公测用户用wing生成的博客

## 系统环境
#### mac、linux和win都可以
#### 手机版可以等一下后面的在线版（有关关键词：github、gitee、在线修改、灵活管理）

## 安装前的版本说明
#### 因为在仓库里的是dev版本
#### dev版本不是特别稳定
#### 如果你运气不好，还有可能是没做完的dev版
#### 所以推荐你看正式版本的安装，开发版本的安装是给开发者查看的，谢谢！

## 安装教程
#### 首先你要保证你的电脑中有python3.5(>=3.5均可)和git（git可选）
#### 如没有可以百度一下属于自己系统的python3和git（git可选）安装方式
#### 作者的python为3.7.3，如果你用你下载的python3运行出现错误，可以试一试使用与作者相同的python3.7.3

### 正式版本的安装：
1. 打开[发行版](https://gitee.com/lingkonggzs/lingkong-wing/releases)，下载`最新``正式`版本的wing的压缩包，然后解压，右键，git bash here
##### 不想安装git的用户可以打开cmd，cd到这个目录下，继续操作
2.  输入`cd lingkong-wing`
3.  去往[主题仓库](https://gitee.com/lingkonggzs/lingkong-wing-theme.git)选择自己喜欢的主题，放入你的lingkong-wing文件夹内，然后编辑theme.json中的主题名为文件夹名
##### 温馨提示：文件夹名不可修改，仓库里是啥名就是啥名
##### 温馨提示：以上这步可以不做，因为wing有一款自带的主题

4. 如果你是windows系统，那在git的bash或cmd中输入`pip install markdown`，如果你是unix系统（macos、linux等），那在终端中输入`pip3 install markdown`
##### 温馨提示：这步有可能出错，如果出错请到readme的最下面找到`问题反馈与帮助`找到提问方法提问
#### 然后你的前期的环境准备工作就完成了


### 开发版本的安装：
1. 在要下载的地方右键，git bash here（前提是你有装git）输入并执行：（Unix的系统可以在终端中cd到你想要装的地方执行）
```
git clone https://gitee.com/lingkonggzs/lingkong-wing.git
```
##### 不想安装git的用户可以下载zip，解压，然后打开cmd，cd到这个目录下，继续操作
2.  输入`cd lingkong-wing`
3.  去往[主题仓库](https://gitee.com/lingkonggzs/lingkong-wing-theme.git)选择自己喜欢的主题，放入你的lingkong-wing文件夹内，然后编辑theme.json中的主题名为文件夹名
##### 温馨提示：文件夹名不可修改，仓库里是啥名就是啥名
##### 温馨提示：以上这步可以不做，因为wing有一款自带的主题
4. 如果你是windows系统，那在git的bash或cmd中输入`pip install markdown`，如果你是unix系统（macos、linux等），那在终端中输入`pip3 install markdown`
##### 温馨提示：这步有可能出错，如果出错请到readme的最下面找到`问题反馈与帮助`找到提问方法提问
#### 然后你的前期的环境准备工作就完成了

## 默认主题的使用说明
#### 首先你要打开theme.json
#### 把theme这项后面的引号里的blog-XXXX改成你复制过来主题的文件夹名
##### 温馨提示：以上这步可以不做，因为wing有一款自带的主题
#### 然后打开你的主题文件夹，打开文件夹下的config.json配置上你喜欢的东西
### 配置内容说明：
1. `user`:用户称呼
2. `photo`:头像地址（本地与网络上的均可）
3. `word-max`:最大的文章值
4. `word-1\2\3-id`:文章id
5. `word-1\2\3-title`:文章标题
6. `word-1\2\3-date`:文章发表日期
7. `word-1\2\3-from`:文章对应的md文件名
8. `right-name`:跳转区名字
9. `right-max`:最大的链接数量
10. `right-1\2\3-id`:链接id
11. `right-1\2\3-id`:链接名字
12. `right-1\2\3-id`:链接跳转地址（本地与网络上的均可）

### 如何新建文章：
1. 打开config.json
2. 复制"1"的那一大个地方,如：
```json
"1":{
    "id": "1",
    "title": "hello",
    "date": "20200418",
    "from": "hello.md"
}
```
这一大个
3. 在上一个大括号（右）的的后面加一个英文`,`
4. 把1，改成上一个数字+1，1+1=2，就把1改成2
5. 改标题（title）、发布时间（date）、文章对应的md文件名（from）
6. 最后拼接起来长这样：
```json
"1":{
    "id": "1",
    "title": "hello",
    "date": "20200418",
    "from": "hello.md"
},
"2":{
    "id": "2",
    "title": "第二个标题",
    "date": "时间",
    "from": "XXXXX.md"
}
```

### 如何新建友链：
1. ![第一步](https://gitee.com/lingkonggzs/lingkong-wing/raw/master/readme/3.png)

2. ![第二步](https://gitee.com/lingkonggzs/lingkong-wing/raw/master/readme/4.png)ps：这幅图中`python3 wing.py s`为旧版操作，新版`python3 wing.py`即可

### ps：win打开命令行的方法是右键，git bash here。unix则要cd到这个目录
### 温馨提示：新版的文件会生成在web文件夹下，如果要上传成果到github、gitee等平台上，请把这个文件夹下的东西全部上传，否则有可能出错
##### 针对上面这行的补充：如果你看到web文件夹下还有.buyaoshan文件，请你不要删掉他，否则这个文件夹下没东西的话，会生成失败。上传到github、gitee等平台上时，你可选择把这个文件一起上传，也可不上传

## 其他主题的使用方法可以打开那个主题的文件夹，里面会自带一个readme哦！
## 其他主题的使用方法可以打开那个主题的文件夹，里面会自带一个readme哦！
## 其他主题的使用方法可以打开那个主题的文件夹，里面会自带一个readme哦！
#### ps：官方的其他主题也会放在项目中，但没被设置成默认主题，可以自行去theme.json改上主题文件夹名。官方的其他主题同上所述，也一样是放在那个主题的文件夹中的readme！

## 以下是几个常用的命令
1.  `python3 wing.py`:激活配置生效
2.  `python3 wing.py z`:查看使用指南
3.  `python3 wing.py v`:查看版本号



## 错误说明
#### 如果你运行时出现错误
#### 请尝试以下方法：
1. 确认是否是按照作者的方法一步一步做的
2. 确认编辑config.json的格式是否错误
#### 如果以上办法无效，请划到最下面问题反馈与帮助查看提问方法

## 版本号说明
#### 版本号的定义为：主版本号.可使用主题数.主程序更新次数-最后更新时间（这个作者老忘记改，请以提交时间为准）
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



## 开发者计划
### 因为依靠官方的力量没法制作那么多的主题，并且按照灵空官方的惯例，这次的wing开发者计划来啦！
### 开发者计划的两大方面的制作
1. html
#### 制作一个html的主题，要求原创、美观
#### html提交到[theme](https://gitee.com/lingkonggzs/lingkong-wing-theme.git)的仓库下的result新建文件夹名叫：类型_名字，如blog_exhibition
2. py
#### 第二个要模仿默认主题的theme.py文件以及config.json文件，制作一款主题
#### 要求：import后就可以生成好，同样生成的结果要原创、美观
#### 温馨提示：读取json文件可以import config，然后通过运行主程序来运行这个主题文件进行测试
#### 做好之后提交到提交到[theme](https://gitee.com/lingkonggzs/lingkong-wing-theme.git)的仓库下新建一个文件夹名叫：类型_名字，如blog_exhibition
### 以上两大方面，第一个方面只要求制作html，较为简单，但是官方的适配时间要很久。第二个方面是制作一个完整主题，直接就可以使用，无bug官方可以立刻上线，与大家见面
### 欢迎参与开发者计划！！！

#### 提交方法
1.  Fork [theme](https://gitee.com/lingkonggzs/lingkong-wing-theme.git)这个仓库仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request

## 问题反馈与帮助
### 方法一：提issues（荐）
##### 打开[这个页面](https://gitee.com/lingkonggzs/lingkong-wing/issues)，然后点击新建issues，接着按照模板填好issues内容，最后点创建就好

### 方法二：联系作者

* 作者钉钉：15392006285（加好友请说明来历）

* 作者qq：2822603942（加好友请说明来历）

##### 推荐第一种方法，第二种方法作者的同意速度没那么快，不太推荐