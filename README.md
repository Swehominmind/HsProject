# HsProject
炉石数据库

# 数据库中期PJ-卡牌库系统设计

> Kevin
>
> Kassadin



## 一、实验题目

炉石传说卡牌库系统的设计与实现。

## 二、实验背景

某卡牌游戏需要一套**卡牌库**系统对卡牌的制造、删除、更新、搜索等方面进行统一管理，同时需要对每个玩家的**个人收藏**中卡牌的合成、分解进行管理。

这里是以"炉石传说"为蓝本。

## 三、主要功能

[]表示可选拓展

### 1. 用户系统

1）系统分为管理员用户和玩家用户。玩家用户在卡牌库中只能查看，在个人收藏中可以对具体卡牌进行合成、分解。管理员用户可以在卡牌库中对卡牌进行制造、删除、更新。

2）管理员用户在系统完成时便已经存在一位。玩家用户则可以后续创建。

3）用户的密码以密文形式保存于数据库中

4）每位用户除了用户名和密码信息外，还有奥术之尘（个人收藏中卡牌合成与分解的货币）的数量。[金币，符文石等]

5）对于卡牌库的查看操作可以以游客身份完成，其余功能只有用户登录了才能进行操作。

### 2. 卡牌库管理

系统中需要维护整个卡牌库目前的所有可用卡牌（包括经典模式[标准模式、狂野模式]），包括卡牌的基本信息{[卡牌ID]，名字， 身材{费用，生命值，攻击力}，稀有度，种族} ，[卡牌适用的版本]，卡牌的效果，[卡牌的描述]，[卡牌的稀有度]，卡牌所属职业[多值关系]，[卡牌语音]，卡牌原画。

[卡牌可特化为 随从minion，法术spell，武器weapon。其中法术的生命值和攻击力为null]

### 3. 卡牌查询

可以使用费用，[身材]，名字，卡牌效果，**关键字**等方式查询卡牌。

**这一部分是极为重要的。**

### 4. 卡牌信息修改

可以修改卡牌名字，卡牌身材，卡牌原画，卡牌效果等，事实上，所有的属性都可以修改。

### 5. 卡牌创建

可以创建新卡牌，[提供这样的创造工具]

![image-20210508170156840](/image/image-20210508170156840.png)

### 6. 个人收藏管理

系统中需要维护每个用户的个人收藏中拥有的卡牌及其库存数量。效果图如下:

![image-20210508170535226](/image/image-20210508170535226.png)

### 7. 个人收藏中卡牌的查询

可以使用费用，[身材]，名字，卡牌效果，**关键字**等方式查询卡牌。

### 8. 奥术之尘货币系统

对于个人收藏中卡牌的分解与合成，[未离开分解/合成页面时允许**撤回**]



合成，这时个人收藏的库存要相应地增加，**但是，本系统规定同一卡牌库存不可因合成超过2**

 <img src="/image/image-20210508171057696.png" alt="/image/image-20210508171057696" style="zoom:25%;" />

分解：

 <img src="/image/image-20210508171031081.png" alt="/image/image-20210508171031081" style="zoom:25%;" />



### 9. [商城系统+财务管理+查看账单]

商城中可以用金币或者符文石购买卡牌包。

每次购买会为系统的财务账户中添加一条账单记录。

允许查看某玩家用户在某段时间内财务账户的收入或支出记录。



## 三、ER图设计

![img](/image/66650F4ECDA00E50AD7B521DAB502BCE.png)



## 四、实验分工

初步分工：

Kassadin完成基础的需求文档和内部数据库与系统的实现，

Kevin完成数据库设计和界面UI的实现。

查询卡牌部分以及索引的建立以及各种拓展想法在后续共同讨论完善。

UI效果图，`html`格式

![image-20210508165518426](/image/image-20210508165518426.png)

