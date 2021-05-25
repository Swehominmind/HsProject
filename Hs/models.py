from django.db import models


# Create your models here.


# 职业列表
class SummonerClass(models.Model):
    name = models.IntegerField(choices=(
        (0, '中立'),
        (1, '德鲁伊'),
        (3, '猎人'),
        (4, '法师'),
        (5, '圣骑士'),
        (6, '牧师'),
        (7, '盗贼'),
        (8, '萨满'),
        (9, '恶魔猎手')
    ))


# 关键词及其效果
class Keyword(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=64)


# 卡牌类
class Card(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    # 类型三选一: spell, minion, weapon
    type = models.IntegerField(choices=(
        (1, '随从'),
        (2, '武器'),
        (3, '法术')
    ))

    # 稀有度
    rarity = models.IntegerField(choices=(
        (0, '基本'),
        (1, '普通'),
        (2, '稀有'),
        (3, '史诗'),
        (4, '传说')
    ))

    # 所属版本
    set = models.CharField(choices=(
        ('Basic', '基本'),
        ('Classic', '经典')
    ))

    # 是否可以合成
    collectible = models.BooleanField(default=1)

    # 允许没有关键词, 这里隐含一个关系表
    keyword = models.ManyToManyField(Keyword, blank=True)

    # 身材三项
    cost = models.IntegerField()
    attack = models.IntegerField()
    health = models.IntegerField()

    # 这里隐含一个关系表
    # 每张卡牌属于的职业数量是不确定的
    # 有的是中立卡，所有职业可用。有的是三职业卡（暗金教），有的是双职业卡（通灵学院）
    # 默认为中立卡
    card_class = models.ManyToManyField(SummonerClass, default=0)

    # 卡牌描述
    description = models.CharField(max_length=64)

    # 种族
    race = models.CharField(max_length=64, blank=True)

    # 以下是可选拓展
    # cost_to_craft
    # disenchanting_yield
    # artist
    # golden


# 账户
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    gold = models.IntegerField(default=0)
    arc_dust = models.BigIntegerField(default=0)

    # 这里隐含一个关系表
    # 每个玩家的账户都对应一组卡牌收藏
    collection = models.ManyToManyField(Card)
