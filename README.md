# ai_ladder
ai_ladder plugin

```
这是一个基于 MCP-Go 的 AI 推理与工具执行服务端组件，通过 SSE 向前端实时推送 AI 推理和工具调用的过程，最终输出结果，并持久化历史记录。
```
### MCP  Gateway 插件地址
```
https://plugin.gin-vue-admin.com/details/111 
```
### MCP 流程图
```
+----------------------+
| 用户发起对话请求     |
+----------------------+
           |
           v
+----------------------------+
| 初始化上下文 + 模型信息   |
| ConnectLoop 连接 MCP SSE |
+----------------------------+
           |
           v
+---------------------------+
| 获取工具列表（ListTools）|
+---------------------------+
           |
           v
+----------------------------------------+
|      进入推理循环（直到终止）          |
+----------------------------------------+
           |
           v
+-----------------------------------------------+
| LLM 推理下一个工具（ExtractNextTool）         |
| --> tool 名称 + 参数 JSON                      |
+-----------------------------------------------+
           |
           v
+----------------------------------+
| resolveParameters                |
| 占位符参数替换 {{tool.field}}    |
+----------------------------------+
           |
           v
+-------------------------------+
| TryCallToolWithRetry          |
| 调用 MCP 工具（含重试机制）   |
+-------------------------------+
           |
           v
+-------------------------------+
| parseAndSendToolResult        |
| SSE 推送返回内容到前端        |
+-------------------------------+
           |
           v
+-----------------------------------------+
| 更新 historyLog + outputs（中间结果）   |
+-----------------------------------------+
           |
           v
       [是否继续？]
        /       \
       /否       \是
      v           v
+--------------------------+       <--- 回到 ExtractNextTool
| finalizeWithLLM          |
| LLM 总结最终回答         |
| SSE 分段输出             |
+--------------------------+
           |
           v
+----------------------------+
| 保存历史记录到数据库      |
+----------------------------+
           |
           v
     +------------------+
     | 推理流程结束 ✅   |
     +------------------+
```
###  配置文件新增
```
ai_ladder:
    mcp_gateway: "http://localhost:8888/sse"
```
### 插件能力
```
该插件全面兼容OpenAI接口标准，无缝对接GPUStack、DeepSeek、阿里云百炼、月之暗面、智谱等业界领先的AI计算平台。

   目前已测试的大模型， openai chat地址:
   GPUStack:    http://localhost/v1-openai/chat/completions
   DeepSeek:    https://api.deepseek.com/chat/completions
   阿里云百炼:    https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions
   月之暗面:     https://api.moonshot.cn/v1/chat/completions
   智谱:         https://open.bigmodel.cn/api/paas/v4/chat/completions
   chatgpt:      https://api.openai.com/v1/chat/completions
   腾讯元宝:       https://api.hunyuan.cloud.tencent.com/v1/chat/completions
   字节豆包:      https://ark.cn-beijing.volces.com/api/v3/chat/completions
   百川大模型:     https://api.baichuan-ai.com/v1/chat/completions
   本地Ollama模型:  http://localhost:11434/v1/chat/completions

该插件支持对接Dify:
    支持工作流， Chatflow， 聊天助手，Agent，文本生成 智能体，需要传参的工作流仅支持，input，number，paragraph 。
```
  
```
### 该插件支持一键导入

#### README(有GIF动图演示☺️☺️)
```
https://github.com/eagle9527/ai_ladder/blob/main/README.md

### 1.功能展示
### 功能 
![Chatflow](https://github.com/eagle9527/ai_ladder/blob/main/Chatflow.png?raw=true)
![文本生成](https://github.com/eagle9527/ai_ladder/blob/main/completionmessages.png?raw=true)
![工作流](https://github.com/eagle9527/ai_ladder/blob/main/workflow.png?raw=true)

![问答](https://github.com/eagle9527/ai_ladder/blob/main/chart.png?raw=true)
![模型](https://github.com/eagle9527/ai_ladder/blob/main/models.png?raw=true)
![历史](https://github.com/eagle9527/ai_ladder/blob/main/history.png?raw=true)

### 动态演示
![演示](https://github.com/eagle9527/ai_ladder/blob/main/yanshi.gif?raw=true)
