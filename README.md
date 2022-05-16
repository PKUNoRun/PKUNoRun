# PKUNoRun

People who don't want to run, unite!

本项目旨在降低科技跑步的门槛, 让不懂计算机的同学也能拥有决定是否跑63km的自主权.

由于人手不足, 本项目暂时只能照顾安卓`PKURunner`的用户, 且所有的用户界面都遵循最简原则.

我们承诺不上传或记录您的学号及其他个人隐私, 如果怀疑这一点, 您可以选择不用或者自行检查代码.

使用本项目的风险由使用者自行承担.

## 更新

我们在 Heroku 上部署了[网页版本](https://pkunorun.herokuapp.com), 这本质上是 https://github.com/PkuRH/PKURunningHelper 的一个包装. 其源码可见[这里](https://github.com/PKUNoRun/PKURunningHelper-Heroku). 该版本可以完成跑步到上传的全部步骤, 因此需要输入用户的学号和密码.

建议**不具备计算机相关技能且信任我们的同学**使用这一版本. 出于安全考虑，仍然建议您在使用该版本后修改校园网账号的密码.

## Usage

由于新版本的`PKURunner`加了商业壳, 对逆向造成了一定困难, 我们暂时没能做到完全消除使用门槛的目标.

使用`adb`连接手机(无需root), 有`java`和`python3`运行环境的* nix用户, 可以执行

```shell
make backup
```

以得到`PKURunner`的内部数据. 手机将弹出一个确认备份的窗口, 建议为备份设置非空的密码(此时需向程序提供该密码), 以减少出现某些错误(指[`1024 bytes written to apps.tar.`](https://github.com/PKUNoRun/PKUNoRun/issues/11))的可能.

执行

```shell
python3 generator/generator.py -db apps/cn.edu.pku.pkurunner/f/data.db -speed 5 -dist 8 -freq 180 -time 19260817-11:45:14
```

可以向数据中插入一条跑步记录.

执行

```shell
make restore
```

可以将经过编辑的数据存储回`PKURunner`. 随后可在`PKURunner`中上传该记录.

## Thanks

本项目需要感谢很多人的努力, 但他们都不愿意公开身份. 要感谢的人有████, ████, ████, ████和████.
