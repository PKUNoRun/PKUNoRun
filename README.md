# PKUNoRun

People who don't want to run, unite!

本项目旨在降低科技跑步的门槛, 让不懂计算机的同学也能拥有决定是否跑63km的自主权.

由于人手不足, 本项目暂时只能照顾安卓PKU Runner的用户, 且所有的用户界面都遵循最简原则.

如果您觉得界面实在不好看或者操作逻辑反人类, 我们欣然认错并表示死活不改. <del>当然您自己写一个也行, 欢迎提PR</del>.

如果您作为iOS用户表示吃柠檬, <del>欢迎向我们捐赠一台Mac用于开发</del>.

我们承诺不上传或记录您的学号及其他个人隐私, 如果怀疑这一点, 您可以选择不用或者自行检查代码.

但我们保留对使用本项目的人数等宏观信息进行统计的权利. 出于对DOS等攻击的防御目的, 我们可能会记录并妥善保管您的ip地址等网络信息. (如果我们怀有恶意, 即使承诺不记录ip地址, 您的ip地址还是可以被记录, 所以不如提醒您存在隐私风险)

对于使用本项目造成的时间数据金钱绩点损失, 我们概不负责并保留不接受任何抱怨的权利(虽然大部分时间还是会接受), 因为没有人逼着您使用本项目.

## Usage

首先下载[pkurunner-target.apk](https://github.com/PKUNoRun/PKUNoRun/releases/download/v1.2.6/pkurunner-target.apk),并登录你的账号.

请注意这个修改后的App与原版App不可共存, 请先上传已有的所有跑步记录再卸载原版, 以免跑步记录丢失. 安装修改版后请先登录您的账号, 再完全退出PKU Runner一次, 使PKU Runner把已有的登录信息写入数据库.

再安装[PKUNoRunHelper](https://github.com/PKUNoRun/PKUNoRunHelper/releases/tag/v1.2.8). 然后在PKURunner的`设置/破解功能`中选择导出`data.db`, 在PKUNoRunHelper中打开, 填写参数, 点按右下角按钮生成跑步记录. 生成完后, 在弹出的界面中选择PKURunner中打开以导入记录.

导入后App由于并不完善, 会停止运行(白屏), 可以手动清除活动并再次进入App. 此时可能能看到你的跑步记录, 也可能看不到. 如果没有出现新的跑步记录, 可以尝试退出App再进入, 或重新导入跑步记录.

导入记录成功后, 通过PKU Runner原有的上传功能上传记录即可.

![示例](https://github.com/PKUNoRun/PKUNoRun/blob/master/demo.gif)

导出`data.db`的功能自然也可以用作备份跑步记录.

如果你的手机已经root因此可以随意访问`/data/data/cn.edu.pku.pkurunner/files`目录下的文件, 那你只需要用到本项目修改`data.db`的部分. 我们相信知道怎么root手机的用户都知道接下来该怎么做.

对于仍然担心安全性的用户, `generator`目录下提供完全本地运行的记录生成工具.

较复杂的网页版记录修改方案不再是首选:

然后在`设置/破解功能`中选择导出`data.db`, 例如使用微信发送给文件传输助手什么的(可能被保存成不同类型的文件), 随后请用文件管理器找到这个文件以备后用.

访问[http://pkunorun.github.io/](http://pkunorun.github.io/), 根据其提示上传`data.db`并修改之. 将被修改过的`data.db`下载到本地后, 从`设置/破解功能`中导入`data.db`. 如果无效果, 登录你的账户以进入设置页面, 多导入几次即可.

## To Developers

在本目录下执行

```shell
    make
```

即可.

如果想为本项目创建其他的patch,请在完成构建后在`pkurunner-target/`目录中尽情修改,并执行`make patch`得到新的`pkurunner.patch`.

如果您想检查我们的代码, 也可以在`pkurunner-target/`目录明中观察, 或者直接看`pkurunner.patch`的内容.

事实上, 本项目设计成前后端形式是为了保密我们所使用的生成数据的算法, 以增加对伪造数据的特征工程的难度.

我们欢迎您根据我们的接口开发新的服务器, 这样即使我们因为种种原因停止服务, 也可以有人接力下去.

## TODO

- [x] 开发一个app, 支持直接分享data.db以及将data.db分享到PKU Runner, 以优化处理data.db时的体验(这样就不用打开浏览器再去文件管理器里找文件了)

- [x] 解决白屏问题, 提高导入data.db时的成功率(虽然可能永远也不做, 多试几次反正能好)

- [ ] 进一步修改伪造数据算法(似乎紧急性也没那么强)

## Thanks

本项目需要感谢很多人的努力, 但他们都不愿意公开身份. 要感谢的人有████, ████, ████, ████和████.

## Q&A

Q:
    为什么在已安装未修改的PKU Runner的情况下无法安装此项目内的PKU Runner?
A:
    修改过的PKU Runner与原版本包名相同但应用签名不同.Android由于安全问题,会阻止新包的安装.

Q:
    为什么导出`data.db`再导回去后登录会失效,从而回到登录界面?
A:
    第一次登录后需要彻底退出PKU Runner,使其将登录信息写入`data.db`.随后再次打开PKU Runner方可导出.

Q:
    为什么这个项目偶尔会出现`PKUWalker`字样?
A:
    因为我们还没完全把名字改过来. 本项目前身是PKUWalker.
</p>
