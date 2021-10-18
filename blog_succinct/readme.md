# blog_succinct主题使用指南

#### 首先你要打开theme.json
#### 把theme这项后面的引号里的blog-XXXX改成blog_succinct
#### 然后打开你的主题文件夹，打开文件夹下的config.json配置上你喜欢的东西
### 配置内容说明：
1. `user`:用户称呼
2. `photo`:头像地址（本地与网络上的均可）
3. `word-max`:最大的文章值
4. `word-1\2\3-id`:文章id
5. `word-1\2\3-title`:文章标题
6. `word-1\2\3-generalization`:文章概要
7. `word-1\2\3-from`:文章对应的md文件名
8. `right-name`:跳转区名字
9. `right-max`:最大的链接数量
10. `right-1\2\3-id`:链接id
11. `right-1\2\3-id`:链接名字
12. `right-1\2\3-id`:链接跳转地址（本地与网络上的均可）
#### 你可以根据以上的描述修改/添加json文件

### 如何新建文章：
1. 打开config.json
2. 复制"1"的那一大个地方,如：
```json
"1":{
    "id": "1",
    "title": "hello",
    "generalization": "欢迎使用官方制作的的第二个主题",
    "from": "hello.md"
}
```
这一大个
3. 在上一个大括号（右）的的后面加一个英文`,`
4. 把1，改成上一个数字+1，1+1=2，就把1改成2
5. 改标题（title）、概要（generalization）、文章对应的md文件名（from）
6. 最后拼接起来长这样：
```json
"1":{
    "id": "1",
    "title": "hello",
    "generalization": "欢迎使用官方制作的的第二个主题",
    "from": "hello.md"
},
"2":{
    "id": "2",
    "title": "第二个标题",
    "generalization": "概要",
    "from": "XXXXX.md"
}
```

### 如何新建友链：
1. ![第一步](https://gitee.com/lkteam/lingkong-wing/raw/master/readme/3.png)

2. ![第二步](https://gitee.com/lkteam/lingkong-wing/raw/master/readme/4.png)ps：这幅图中`python3 wing.py s`为旧版操作，新版`python3 wing.py`即可

### ps：win打开命令行的方法是右键，git bash here。（也可以双击打开）unix则要cd到这个目录
### 温馨提示：新版的文件会生成在web文件夹下，如果要上传成果到github、gitee等平台上，请把这个文件夹下的东西全部上传，否则有可能出错
##### 针对上面这行的补充：如果你看到web文件夹下还有.buyaoshan文件，请你不要删掉他，否则这个文件夹下没东西的话，会生成失败。上传到github、gitee等平台上时，你可选择把这个文件一起上传，也可不上传


## 问题反馈与帮助
### 方法一：提issues（荐）
##### 打开[这个页面](https://gitee.com/lkteam/lingkong-wing/issues)，然后点击新建issues，接着按照模板填好issues内容，最后点创建就好

### 方法二：联系作者

* 作者钉钉：15392006285（加好友请说明来历）

* 作者qq：2822603942（加好友请说明来历）

##### 推荐第一种方法，第二种方法作者的同意速度没那么快，不太推荐