# PKUNoRun

People who don't want to run, unite!

本项目旨在降低科技跑步的门槛, 让不懂计算机的同学也能拥有决定是否跑63km的自主权.

由于人手不足, 本项目暂时只能照顾安卓`PKURunner`的用户, 且所有的用户界面都遵循最简原则.

我们承诺不上传或记录您的学号及其他个人隐私, 如果怀疑这一点, 您可以选择不用或者自行检查代码.

使用本项目的风险由使用者自行承担.

## Usage

由于新版本的`PKURunner`加了商业壳, 对逆向造成了一定困难, 我们暂时没能做到完全消除使用门槛的目标.

使用`adb`连接手机(无需root), 有`java`和`python3`运行环境的* nix用户, 可以执行

```shell
make backup
```

以得到`PKURunner`的内部数据.

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
