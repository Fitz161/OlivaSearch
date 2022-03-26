## OlivaSearch

### 介绍
基于 [OlivOS](https://github.com/OlivOS-Team/OlivOS) 框架的搜索插件

### 下载
从本项目下载源码，压缩为zip格式并将后缀名改为opk放入 `plugin/app` 目录下

### 配置
- 本插件依赖requests和lxml，OlivOS默认已安装该模块

### 使用说明
- `搜索 帮助` 查看本插件使用帮助
- `搜索[格式] [待搜索关键词]` 进行搜索操作，示例:`百度 你好` 和 `搜索2 你好`
- 可用搜索格式: 
  - 百度/搜索1：百度百科  
  - 搜索2：萌娘百科
  - 搜索3：touhouwiki
  - 搜索4：wikipedia
- 由于`百度`较为常用，为避免冲突，使用百度进行搜索时`百度`二字后需要跟一个空格。
  
### 指令扩展
本插件具有方便的指令扩展功能<br>
在`msgReply.py`文件中使用以下格式即可定义新指令
```
@add_command('新命令')
def func_name(plugin_event, _):
    ...
    return '待发送的消息'
```
使用 `搜索 新命令` 方式调用指令<br>
**注意**：在编写新指令的过程中一定要知道自己在做什么，否则可能会导致无法意料的后果