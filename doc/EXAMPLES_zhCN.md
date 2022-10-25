# 📚 配置示例

在这一页，你可以看到各种存在配置的例子。为了简洁起见(文本和文件是不需要解释的）只显示 `[Presence]` 部分，除非有一些特殊的东西需要在文本/文件配置中查看的情况。


## 静态配置

如果你不希望你的状态是动态的（例如，根据环境改变）。
你可以坚持使用静态配置：

```ini
[Presence]
# 将此设置为'True'将确保配置始终处于激活状态.
Condition = True
# 最高的优先级将意味着它将永远被选为状态配置.
Priority = 1000
# 'False'将禁止对文本中的变量进行评估.
Dynamic = False
```

## 后备配置

如果没有可用的活动配置，子模组将清除状态显示（但会保持连接，以便当可用时时再次快速显示状态）。

为了确保至少有东西被显示出来，有一个*后备*配置是很有用的。



```ini
[Presence]
# 因为这被设置为'True'，所以这个配置将始终处于激活状态。
Condition = True
# 具有最低的优先级，这个配置只有在没有其他配置可用时才会激活
Priority = -1000
Dynamic = True
```

## 基于一天中的时间的配置

使用`mas_globals.time_of_day_4state`变量，你可以创建一个配置，只有在你想要的时间段才会被激活。可用的值（放在`==`后面的值， 需要带`""`）

* `morning`
* `afternoon`
* `evening`
* `night`

```ini
[Presence]
Condition = mas_globals.time_of_day_4state == "morning"
Priority = -950
Dynamic = True
```

## 基于天气的配置

使用`mas_current_weather`，我们可以创建一个配置，当Monika的世界中出现某种类型的天气时，它就会被激活。

下面是当前可用的值的列表（与其他例子不同, 这些值不是字符串，而且是故意不加引号的）。

* `mas_weather_def`
* `mas_weather_rain`
* `mas_weather_snow`
* `mas_weather_thunder`
* `mas_weaher_overcast`

```ini
[Presence]
Condition = mas_current_weather == mas_weather_rain
Priority = -995
Dynamic = True
```

## 基于话题的配置

使用自定义变量`event_label`，你可以创建一个配置，当玩家进入某个主题时，就会选择该配置。

```ini
[Presence]
Condition = event_label == "monika_hemispheres"
Priority = -20
Dynamic = True
```

话题名称没有一个可用的变量清单，但你可以研究一下 [Monika After Story](https://github.com/Monika-After-Story/MonikaModDev/blob/master/Monika%20After%20Story/game/script-topics.rpy#L868)的源代码，从那里获得事件标签和从Submod中获得自定义标签