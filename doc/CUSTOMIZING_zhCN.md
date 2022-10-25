# 🔧 自定义 Discord Presence Submod

虽然 Discord Presence Submod 配置系统被设计成简单易懂，但你可能需要一个帮助来了解什么是什么，以及如何使用它，而这份文件正是你所需要的。

如果你在找如何覆盖默认的配置的方法，可以查看[DEFAULTS.md](DEFAULTS.md)获取详细信息

## Examples

如果你想通过例子来学习，你不妨看看`config/`文件夹，其中包含了所有被维护的配置文件，这些文件都有很好的注释和记录，以方便你的理解。

另外，也可以看看[EXAMPLES.md](EXAMPLES.md)页面来学习一些简单的理论知识。

## 基础

### Presence 配置文件

Discord Rich Presence 基于 *Presence Configs*, 这些文件位于
`config/` 文件夹，描述了活动的条件，信息等

文件名对submod来说没有任何意义，只是帮助你区分出存在的配置；但是，配置文件必须有以下扩展名之一: `.cfg`, `.ini`或`.conf`，任何其他扩展名的文件将被忽略。

### 条件和优先权

为了反映游戏的变化，让你根据一些输入数据显示不同的活动，存在配置有*条件*(conditional)和*优先权*(priorities)，这些条件和优先权结合在一起，决定在下一个循环中选择哪个配置。

*条件*是一个Python表达式，它在全局MAS范围内进行评估（这意味着你可以访问任何变量）。当条件的表达式为True时(或者转换为bool类型为True)，这个配置将在下次更新时应用。

当然，也有一些情况是，同时存在多个可用的配置。
这时*Priority*就派上用场了。每个在场配置都有优先级。在评估了配置条件并将符合条件的配置排列之后，优先级较高的将被使用。
（eg: 两个符合条件的配置的值为50和100，其中一个值为100的配置将被使用。）
如果两个配置的优先级相同，那么无法确定哪一个会被应用。

### 可变插值

在活动信息和图片标题中，可以使用Ren'Py的标准语法 `[variable_name]` 插入变量; 此外，Python语法在一定程度上被支持，也可以直接调用函数: `[function(arguments...)]`.

插值是在全局范围内进行的，这意味着所有MAS（和子模组）的变量都可以被访问（如`[m_name]`，`[player]`等）。

## 进阶概念

### 扩展

扩展内容不是Discord Presence Submod的独有功能，你可以创建一个.rpy文件，直接管理变量

Discord Presence Submod ships with few extensions maintained by project creators
and maintainers:

* `fom-custom-vars.rpy` 提供了自定义变量框架，用于注册和更新自定义变量，更新可用于表达式和插值的自定义变量。
* `fom-events.rpy` 提供了与即将发生的日历有关的自定义变量。
* `fom-functions.rpy` 提供自定义函数，可以在插值中使用。
* `fom-locations.rpy` 用于显示当前活动的背景  